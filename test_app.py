from app import create_app


def test_home_route_returns_200():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_post_clients_returns_201():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/clients",
        json={
            "name": "Asha",
            "weight": 60,
            "program": "Fat Loss (FL) – 3 day",
        },
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Asha"
    assert data["calories"] == 1320


def test_get_clients_returns_200():
    app = create_app()
    client = app.test_client()

    client.post(
        "/clients",
        json={
            "name": "Rahul",
            "weight": 70,
            "program": "Beginner (BG)",
        },
    )

    response = client.get("/clients")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
