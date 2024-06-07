from datetime import datetime
from uuid import UUID

from app.utils.serialize_for_json import serialize_for_json


def test_serialize_for_json():
    data = {
        "uuid": UUID("dd093495-b637-4ff8-bf2c-eb99d0f88031"),
        "created_at": datetime.fromisoformat("2024-06-03T18:38:35.447990"),
        "status": "Aguardando Check-in",
        "check_in": datetime.fromisoformat("2024-09-15T08:30:00"),
        "check_out": datetime.fromisoformat("2024-09-18T12:30:00"),
        "guest": {
            "document": "03093331056",
            "name": "John",
            "surname": "Doe",
            "phone": "4832395853",
            "country": "Brazil",
            "created_at": datetime.fromisoformat("2024-05-22T10:56:45"),
        },
        "accommodation": {
            "uuid": UUID("bcadaaf8-a036-42d5-870c-de7b24792abf"),
            "name": "Domo",
            "status": "Disponível",
            "total_guests": 2,
            "single_beds": 0,
            "double_beds": 1,
            "min_nights": 2,
            "price": 590,
            "created_at": datetime.fromisoformat("2000-01-01T00:00:00"),
            "amenities": [
                "ar-condicionado",
                "wifi",
                "tv",
                "frigobar",
                "ducha",
                "cozinha",
                "toalhas",
            ],
        },
    }

    new_obj = serialize_for_json(data)
    assert isinstance(new_obj["uuid"], str)
    assert isinstance(new_obj["created_at"], str)
    assert isinstance(new_obj["accommodation"]["uuid"], str)
    assert isinstance(new_obj["guest"]["created_at"], str)