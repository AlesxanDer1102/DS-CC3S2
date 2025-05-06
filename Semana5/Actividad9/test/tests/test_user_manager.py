import pytest

from src.user_manager import UserManager, UserAlreadyExistsError

def test_agregar_usuario_exitoso():

    manager= UserManager()
    username="diego"
    password="password"
    manager.add_user(username, password)
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."
