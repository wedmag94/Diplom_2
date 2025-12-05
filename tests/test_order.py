import pytest
import allure

from stellar_burgers_api import UserApi, OrderApi
from data import OrderBody, MessageText


class TestOrder:

    @allure.title("Создание заказа с авторизацией и валидными ингредиентами")
    @allure.description(
        "Проверяем, что авторизованный пользователь может создать заказ с валидными ингредиентами"
    )
    def test_successfull_creating_order_with_authorization(self, register_user):
        _, user_data = register_user
        UserApi.auth_user(user_data)
        ingredients_body = OrderBody.BODY_WITH_VALID_HASH
        response_order = OrderApi.create_order(ingredients_body)
        assert response_order.status_code == 200
        response_json = response_order.json()
        assert "name" in response_json
        assert "order" in response_json
        assert response_json["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_creating_order_without_authorization(self):
        ingredients_body = OrderBody.BODY_WITH_VALID_HASH
        response_order = OrderApi.create_order(ingredients_body)
        assert response_order.status_code == 200
        response_json = response_order.json()
        assert "name" in response_json
        assert "order" in response_json
        assert response_json["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка, что невозможно создать заказ без ингредиентов")
    def test_creating_order_without_ingredients(self):
        ingredients_body = OrderBody.BODY_WITHOUT_INGREDIENTS
        response_order = OrderApi.create_order(ingredients_body)
        assert response_order.status_code == 400
        response_json = response_order.json()
        assert response_json["success"] is False
        assert response_json["message"] == MessageText.MISSING_INGREDIENTS

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description(
        "Проверка, что невозможно создать заказ с неверным хешем ингредиентов"
    )
    def test_creating_order_with_ingredients_invalid_hash(self):
        ingredients_body = OrderBody.BODY_WITH_INVALID_HASH
        response_order = OrderApi.create_order(ingredients_body)
        assert response_order.status_code == 500
