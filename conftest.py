import pytest
import allure

from generator import generate_user_body
from stellar_burgers_api import *


@pytest.fixture  # Фикстура для создания нового пользователя с автоматической очисткой данных после теста
def register_user():
    response_create = None
    user_token = None

    with allure.step("Создание нового пользователя"):
        data = generate_user_body()
        response_create = UserApi.creating_user(data)
        response_json = response_create.json()
        if response_json["success"] is True:
            user_token = response_json.get("accessToken")
        yield response_create, data

    with allure.step("Очистка данных о созданных пользователях после теста"):
        if user_token:
            UserApi.delete_user(user_token)
