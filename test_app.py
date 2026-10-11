from app import app


def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Smart Parking" in response.data


def test_toggle_parking_slot():
    client = app.test_client()
    response = client.post("/toggle/1")

    assert response.status_code == 302