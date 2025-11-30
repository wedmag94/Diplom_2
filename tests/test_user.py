import pytest
import allure

from stellar_burgers_api import UserApi
from data import MessageText
from generator import generate_user_body


class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    @allure.description(
        "Проверяем, что успешный запрос возвращает код ответа 200 и тело ответа содержит поля 'success','user','accessToken','refreshToken'"
    )
    def test_successfull_creating_unique_user(self, register_user):
        response_create, _ = register_user
        assert (
            response_create.status_code == 200
        ), f"Ожидался код ответа 200, получен {response_create.status_code}"
        response_json = response_create.json()
        assert "success" in response_json
        assert "user" in response_json
        assert "accessToken" in response_json
        assert "refreshToken" in response_json

    @allure.step("Создание пользователя, который уже зарегестрирован")
    @allure.description(
        "Проверяем, что при попытке повторной регистрации должен вернуться код 403 и сообщение 'User already exists'"
    )
    def test_impossible_to_create_identical_users(self, register_user):
        first_user, first_data = register_user
        assert first_user.json()["success"] is True
        with allure.step("Повторное создание пользователя"):
            duplication_data = first_data

            response = UserApi.creating_user(duplication_data)
            assert response.status_code == 403
            response_json = response.json()
            assert response_json["success"] is False
            assert response_json["message"] == MessageText.USER_EXISTS

    @allure.title(
        "Проверяем, что при отсутствии одного из обязательных полей возвращается ошибка"
    )
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_no_required_field(self, field):
        data = generate_user_body()
        data.pop(field)
        response = UserApi.creating_user(data)
        assert response.status_code == 403
        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == MessageText.REQUIRED_FIELD_MISSING
