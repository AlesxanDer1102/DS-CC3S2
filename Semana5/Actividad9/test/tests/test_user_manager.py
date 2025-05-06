import pytest
from unittest.mock import MagicMock
from src.user_manager import UserManager, UserAlreadyExistsError

class FakeHashService:

    def hash(self,plain_text:str)->str:
        return f"fakehash:{plain_text}"
    
    def verify(self, plain_text:str, hashed_text:str)->bool:
        return hashed_text == f"fakehash:{plain_text}"

def test_agregar_usuario_exitoso():

    manager= UserManager()
    username="diego"
    password="password"
    manager.add_user(username, password)
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."


def test_autenticar_usuario_exitoso_con_hash():

    hash_service= FakeHashService()
    manager= UserManager(hash_service=hash_service)

    username= "user1"
    password= "password"
    manager.add_user(username, password)

    autenticado=manager.authenticate_user(username, password)

    assert autenticado, "El usuario deberia autenticarse correctamente con lo contraseña correcta."

def test_hash_service_es_llamado_al_agregar_usuario():

    mock_hash_service=MagicMock()
    manager=UserManager(hash_service=mock_hash_service)
    username="spyUser"
    password="spyPass"
    manager.add_user(username, password)

    mock_hash_service.hash.assert_called_once_with(password)

def test_no_se_puede_agregar_usuario_existente_stub():
    # Este stub forzará que user_exists devuelva True
    class StubUserManager(UserManager):
        def user_exists(self, username):
            return True

    stub_manager = StubUserManager()
    with pytest.raises(UserAlreadyExistsError) as exc:
        stub_manager.add_user("cualquier", "1234")

    assert "ya existe" in str(exc.value)