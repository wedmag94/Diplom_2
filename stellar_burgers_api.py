import requests
import allure
from generator import *
from curl import Url


class UserApi:

    @staticmethod
    @allure.step("Создание пользователя")
    def creating_user(body=None):
        return requests.post(Url.USER_REGISTER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Авторизация пользователя")
    def auth_user(auth_data):
        return requests.post(Url.USER_AUTH_ENDPOINT, json=auth_data)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(user_token):
        headers = {"Authorization": user_token}
        return requests.delete(Url.USER_ENDPOINT, headers=headers)


class OrderApi:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(ingredients_body):
        return requests.post(Url.CREATE_ORDER_ENDPOINT, json=ingredients_body)
