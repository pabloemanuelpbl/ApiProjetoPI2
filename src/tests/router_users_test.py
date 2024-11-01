from fastapi.testclient import TestClient
from routes.users import UserCreate

import time
timestamp = time.time()

def test_post_users(client: TestClient) -> None:
    payload = UserCreate(
        username='pablo',
        email=f"{timestamp}abc@cc.c",
        hashed_password="secret"
    ).model_dump()

    response = client.post('/users', json=payload)
    body = response.json()
    assert response.status_code == 201
    assert isinstance(body, dict)
    assert len(body) > 0
    

def test_post_users_duplicate(client: TestClient) -> None:
    payload = UserCreate(
        username='pablo',
        email=f"{timestamp}abc@cc.c",
        hashed_password="secret"
    ).model_dump()

    response = client.post('/users', json=payload)
    body = response.json()
    assert response.status_code == 400
    assert body["detail"] == "Email já cadastrado."

def test_post_users_field_required( client: TestClient):
    username='olbap'
    email=f"{timestamp}fieldrequired@cc.c"
    hashed_password="secret"

    not_hash = {"username": username, "email": email}
    not_name = {"hashed_password": hashed_password, "email": email}
    not_mail = {"username": username,"hashed_password": hashed_password}
    response_not_hash = client.post('/users', json=not_hash)
    response_not_name = client.post('/users', json=not_name)
    response_not_mail = client.post('/users', json=not_mail)

    not_hash_body = response_not_hash.json()
    not_name_body = response_not_name.json()
    not_mail_body = response_not_mail.json()

    assert response_not_hash.status_code == 422
    assert not_hash_body['detail'][0]['type'] == "missing"
    assert not_hash_body['detail'][0]['msg'] == "Field required"

    assert response_not_name.status_code == 422
    assert not_name_body['detail'][0]['type'] == "missing"
    assert not_name_body['detail'][0]['msg'] == "Field required"

    assert response_not_name.status_code == 422
    assert not_name_body['detail'][0]['type'] == "missing"
    assert not_name_body['detail'][0]['msg'] == "Field required"


def test_get_users(client: TestClient) -> None:
    response = client.get('/users')
    body = response.json()
    assert response.status_code == 200
    assert isinstance(body, list)
    assert isinstance(body[0], dict)


def test_get_user_by_id(client: TestClient) -> None:
    response = client.get('/users/1')
    body = response.json()
    assert response.status_code == 200
    assert isinstance(body, dict)
    assert len(body) > 0

def test_delete_user_by_id(client: TestClient) -> None:
    response = client.delete('/users/1')
    assert response.status_code == 204

def test_get_user_deleted_by_id(client: TestClient) -> None:
    response = client.get('/users/1')
    body = response.json()
    assert response.status_code == 404
    assert isinstance(body, dict)
    assert len(body) > 0
    assert body['detail'] == "Not Found"
