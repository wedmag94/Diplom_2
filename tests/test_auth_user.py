import pytest
import allure

from stellar_burgers_api import UserApi
from data import MessageText, DataForUser


class TestAuthUser:

    @allure.title("Успешный вход зарегистрированного пользователя")
    def test_successful_login_registered_user(self, register_user):
        _, user_data = register_user
        auth_data = {"email": user_data["email"], "password": user_data["password"]}
        response_auth = UserApi.auth_user(auth_data)
        assert response_auth.status_code == 200
        response_json = response_auth.json()
        assert response_json["success"] is True
        assert "accessToken" in response_json
        assert "refreshToken" in response_json
        assert "user" in response_json

    @allure.title("Попытка входа с неверным логином или паролем")
    @allure.description(
        "Проверка, что при попытке входа с неверном логином или паролем в ответе на запрос приходит код 401 и сообщение 'email or password are incorrect'"
    )
    @pytest.mark.parametrize(
        "field, incorrect_value",
        [
            ("email", DataForUser.USER_AUTH_BODY["email"]),
            ("password", DataForUser.USER_AUTH_BODY["password"]),
        ],
    )
    def test_incorrect_email_or_password(self, register_user, field, incorrect_value):
        _, user_data = register_user
        auth_data = {"email": user_data["email"], "password": user_data["password"]}
        auth_data[field] = incorrect_value
        response_auth = UserApi.auth_user(auth_data)
        assert response_auth.status_code == 401
        response_json = response_auth.json()
        assert response_json["success"] is False
        assert response_json["message"] == MessageText.INCORRECT_EMAIL_OR_PASSWORD
