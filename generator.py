from faker import Faker

fake = Faker()


def generate_user_body():
    body = {
        "email": fake.email(),
        "password": fake.password(length=8),
        "name": fake.user_name(),
    }
    return body
