from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_login_com_sucesso():
    resposta = client.post(
        "/auth/login",
        json={
            "email": "admin@email.com",
            "senha": "123456"
        }
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["mensagem"] == "Autenticação realizada com sucesso"
    assert "token" in dados
    assert dados["token"] == "token-fake-123"


def test_login_com_credenciais_invalidas():
    resposta = client.post(
        "/auth/login",
        json={
            "email": "usuario_errado@email.com",
            "senha": "senha_errada"
        }
    )

    assert resposta.status_code == 401

    dados = resposta.json()

    assert dados["detail"] == "Credenciais inválidas"