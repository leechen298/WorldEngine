import pytest
from pydantic import ValidationError


def _event_classes():
    from app.schemas.event import Event, EventPage, EventRef, EventStep, EventStepPage

    return Event, EventPage, EventRef, EventStep, EventStepPage


def _event_data(**overrides):
    data = {
        "id": "event-1",
        "tick_id": 1,
        "world_time_seconds": 30,
        "type": "tick",
        "source": "system",
        "payload": {"message": "hello"},
        "created_at": "2026-05-24T10:00:00Z",
    }
    data.update(overrides)
    return data


def test_imports_event_ref_and_event_schema_classes() -> None:
    Event, _, EventRef, _, _ = _event_classes()

    assert Event.__name__ == "Event"
    assert EventRef.__name__ == "EventRef"


def test_existing_event_construction_without_refs_still_works() -> None:
    Event, _, _, _, _ = _event_classes()

    event = Event(**_event_data())

    assert event.payload == {"message": "hello"}
    assert event.refs == []


def test_event_accepts_refs_with_role_and_metadata() -> None:
    Event, _, EventRef, _, _ = _event_classes()

    event = Event(
        **_event_data(
            refs=[
                {
                    "id": "agent-1",
                    "kind": "agent",
                    "role": "actor",
                    "metadata": {"source": "test"},
                }
            ]
        )
    )

    assert event.refs == [
        EventRef(
            id="agent-1",
            kind="agent",
            role="actor",
            metadata={"source": "test"},
        )
    ]


@pytest.mark.parametrize("payload", [{"id": "", "kind": "agent"}, {"id": "agent-1", "kind": ""}])
def test_event_ref_rejects_empty_id_and_kind(payload: dict) -> None:
    _, _, EventRef, _, _ = _event_classes()

    with pytest.raises(ValidationError):
        EventRef(**payload)


def test_event_ref_role_is_optional_and_metadata_defaults_to_empty_dict() -> None:
    _, _, EventRef, _, _ = _event_classes()

    event_ref = EventRef(id="cell-1", kind="cell")

    assert event_ref.role is None
    assert event_ref.metadata == {}


def test_event_ref_accepts_free_form_metadata_without_interpretation() -> None:
    _, _, EventRef, _, _ = _event_classes()
    metadata = {
        "labels": ["alpha", "beta"],
        "weights": {"primary": 1, "secondary": 0.5},
        "active": True,
    }

    event_ref = EventRef(id="ref-1", kind="generic_ref", metadata=metadata)

    assert event_ref.metadata == metadata


def test_event_model_dump_and_validate_round_trip_preserves_refs() -> None:
    Event, _, _, _, _ = _event_classes()
    original = Event(
        **_event_data(
            refs=[
                {
                    "id": "cell-1",
                    "kind": "world_cell",
                    "role": "location",
                    "metadata": {"depth": 0},
                }
            ]
        )
    )

    dumped = original.model_dump()
    reconstructed = Event.model_validate(dumped)

    assert dumped["refs"] == [
        {
            "id": "cell-1",
            "kind": "world_cell",
            "role": "location",
            "metadata": {"depth": 0},
        }
    ]
    assert reconstructed == original


def test_event_page_validates_events_with_and_without_refs() -> None:
    Event, EventPage, _, _, _ = _event_classes()

    page = EventPage(
        items=[
            Event(**_event_data(id="event-1")),
            Event(**_event_data(id="event-2", refs=[{"id": "agent-1", "kind": "agent"}])),
        ],
        has_more=False,
        limit=20,
    )

    assert page.items[0].refs == []
    assert page.items[1].refs[0].id == "agent-1"


def test_event_step_and_event_step_page_validate_nested_event_refs() -> None:
    Event, _, _, EventStep, EventStepPage = _event_classes()
    event = Event(**_event_data(refs=[{"id": "resource-1", "kind": "resource"}]))

    step = EventStep(
        tick_id=1,
        world_time_seconds=30,
        event_count=1,
        created_at="2026-05-24T10:00:00Z",
        items=[event],
    )
    page = EventStepPage(items=[step], has_more=False, limit=20)

    assert page.items[0].items[0].refs[0].kind == "resource"
