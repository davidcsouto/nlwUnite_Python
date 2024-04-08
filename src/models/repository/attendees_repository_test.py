import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = "meu-uuid-e-nois"
    attendees_info = {
        "uuid": "meu_uuid_attendee",
        "name": "atendee name",
        "email": "email@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)


@pytest.mark.skip(reason="Teste consulta a attendee registrado em evento")
def test_get_attendee_bagde_by_id():
    attendee_id = "meu_uuid_attendee"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_bagde_by_id(attendee_id)

    print(attendee)
    print(attendee.title)
