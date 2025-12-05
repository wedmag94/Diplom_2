class DataForUser:
    USER_AUTH_BODY = {"email": "naruto@ya.ru", "password": "12345qq"}


class MessageText:
    USER_EXISTS = "User already exists"
    REQUIRED_FIELD_MISSING = "Email, password and name are required fields"
    INCORRECT_EMAIL_OR_PASSWORD = "email or password are incorrect"
    MISSING_INGREDIENTS = "Ingredient ids must be provided"


class OrderBody:
    BODY_WITH_VALID_HASH = {
        "ingredients": ["61c0c5a71d1f82001bdaaa79", "61c0c5a71d1f82001bdaaa77"]
    }
    BODY_WITH_INVALID_HASH = {"ingredients": ["5678909876"]}
    BODY_WITHOUT_INGREDIENTS = {"ingredients": []}
