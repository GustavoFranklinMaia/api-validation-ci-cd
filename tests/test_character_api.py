import pytest
from src.api_client import RickAndMortyClient


client = RickAndMortyClient()


@pytest.mark.smoke
@pytest.mark.integration
def test_get_character_rick_by_id():
    r = client.get_character_by_id(1)

    assert r.status_code == 200
    assert r.json is not None

    body = r.json
    assert body["id"] == 1
    assert body["name"] == "Rick Sanchez"
    assert body["status"] in {"Alive", "Dead", "unknown"}  # API may change in some episodes, but Rick is usually Alive.
    assert body["species"] == "Human"
    assert "origin" in body and "name" in body["origin"]
    assert isinstance(body["episode"], list) and len(body["episode"]) > 0


@pytest.mark.integration
def test_search_character_by_name_returns_results():
    r = client.search_character("Rick")

    assert r.status_code == 200
    assert r.json is not None

    body = r.json
    assert "results" in body
    assert len(body["results"]) > 0

    # validates the shape of the first item
    first = body["results"][0]
    assert "id" in first
    assert "name" in first
    assert "status" in first


@pytest.mark.integration
def test_get_character_invalid_id_returns_404():
    r = client.get_character_by_id(999999)

    assert r.status_code == 404
    # the API normally returns {“error”: “...”}
    assert r.json is not None
    assert "error" in r.json


@pytest.mark.integration
def test_response_time_under_reasonable_limit():
    r = client.get_character_by_id(1)

    assert r.status_code == 200
    # portfolio limit =>concern for performance
    assert r.elapsed_ms < 1500
