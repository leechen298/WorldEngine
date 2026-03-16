from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from app.world.validation.registry import ParamRegistry, ParamRule
from app.world.validation.types import ValidationError, ValidationResult


class ParamValidator:
    _allowed_ops = {"add", "set", "remove"}

    def __init__(self, registry: ParamRegistry) -> None:
        self._registry = registry

    def validate(self, patches: list[object]) -> ValidationResult:
        errors: list[ValidationError] = []

        for patch in patches:
            errors.extend(self._validate_patch(patch))

        return ValidationResult(ok=not errors, errors=errors)

    def _validate_patch(self, patch: object) -> list[ValidationError]:
        op = getattr(patch, "op", None)
        path = getattr(patch, "path", "") or ""
        value = getattr(patch, "value", None)

        if op not in self._allowed_ops:
            return [
                ValidationError(
                    path=path,
                    reason="invalid_op",
                    expected=sorted(self._allowed_ops),
                    got=op,
                    detail="Patch op must be one of add, set, or remove.",
                )
            ]

        if self._registry.is_reserved_path(path):
            return [
                ValidationError(
                    path=path,
                    reason="reserved_prefix",
                    detail="Reserved params cannot be modified.",
                )
            ]

        rule = self._registry.get_rule(path)
        if rule is None:
            return [
                ValidationError(
                    path=path,
                    reason="unknown_path",
                    detail="Param path is not registered as writable.",
                )
            ]

        if op == "remove":
            return []

        if value is None:
            return [
                ValidationError(
                    path=path,
                    reason="missing_value",
                    detail="Patch value is required for add/set operations.",
                )
            ]

        raw_value = value
        if isinstance(value, Mapping) and "value" in value:
            if not rule.allow_structured:
                return [
                    ValidationError(
                        path=path,
                        reason="type_mismatch",
                        expected=rule.expected_type,
                        got="structured",
                        detail="Structured param values are not allowed for this path.",
                    )
                ]
            raw_value = value["value"]

        type_error = self._validate_type(path, raw_value, rule)
        if type_error is not None:
            return [type_error]

        range_error = self._validate_constraints(path, raw_value, rule)
        if range_error is not None:
            return [range_error]

        return []

    def _validate_type(
        self,
        path: str,
        raw_value: Any,
        rule: ParamRule,
    ) -> ValidationError | None:
        expected_type = rule.expected_type

        if expected_type == "int":
            if isinstance(raw_value, bool) or not isinstance(raw_value, int):
                return self._type_mismatch(path, expected_type, raw_value)
            return None

        if expected_type == "bool":
            if not isinstance(raw_value, bool):
                return self._type_mismatch(path, expected_type, raw_value)
            return None

        if expected_type == "float":
            if isinstance(raw_value, bool) or not isinstance(raw_value, (int, float)):
                return self._type_mismatch(path, expected_type, raw_value)
            return None

        if expected_type == "string":
            if not isinstance(raw_value, str):
                return self._type_mismatch(path, expected_type, raw_value)
            return None

        if expected_type == "json" and not self._is_json_value(raw_value):
            return self._type_mismatch(path, expected_type, raw_value)

        return None

    def _validate_constraints(
        self,
        path: str,
        raw_value: Any,
        rule: ParamRule,
    ) -> ValidationError | None:
        minimum = rule.constraints.get("min")
        if minimum is not None and raw_value < minimum:
            return ValidationError(
                path=path,
                reason="out_of_range",
                expected={"min": minimum, "max": rule.constraints.get("max")},
                got=raw_value,
                detail=f"Value must be greater than or equal to {minimum}.",
            )

        maximum = rule.constraints.get("max")
        if maximum is not None and raw_value > maximum:
            return ValidationError(
                path=path,
                reason="out_of_range",
                expected={"min": rule.constraints.get("min"), "max": maximum},
                got=raw_value,
                detail=f"Value must be less than or equal to {maximum}.",
            )

        return None

    def _type_mismatch(
        self,
        path: str,
        expected_type: str,
        raw_value: Any,
    ) -> ValidationError:
        return ValidationError(
            path=path,
            reason="type_mismatch",
            expected=expected_type,
            got=self._describe_type(raw_value),
            detail=f"Param value does not match expected type {expected_type}.",
        )

    @staticmethod
    def _describe_type(value: Any) -> str:
        if isinstance(value, bool):
            return "bool"
        if value is None:
            return "null"
        return type(value).__name__

    @classmethod
    def _is_json_value(cls, value: Any) -> bool:
        if value is None:
            return True
        if isinstance(value, (str, int, float, bool)):
            return True
        if isinstance(value, list):
            return all(cls._is_json_value(item) for item in value)
        if isinstance(value, Mapping):
            return all(
                isinstance(key, str) and cls._is_json_value(item)
                for key, item in value.items()
            )
        return False
