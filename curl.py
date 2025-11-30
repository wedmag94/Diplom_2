class Url:
    BASE_URL = "https://stellarburgers.education-services.ru"

    CREATE_ORDER_ENDPOINT = BASE_URL + "/api/orders"  # эндпоинт для создания заказа

    USER_REGISTER_ENDPOINT = (
        BASE_URL + "/api/auth/register"
    )  # эндпоинт для регистрации пользователя

    USER_AUTH_ENDPOINT = (
        BASE_URL + "/api/auth/login"
    )  # эндпоинт для авторизации пользователя

    USER_ENDPOINT = (
        BASE_URL + "/api/auth/user"
    )  # эндпоинт для получения, обновления и удаления данных о пользователе
