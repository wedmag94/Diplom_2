## Дипломный проект. Задание 2: Автотесты для API
<hr>

## Студент: Чумбарева Лидия

## <h>Когорта: #32</h>
<hr>

## <h>Project: Stellar Burgers</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:green">Описание файлов проекта:</h3>

| Название файла          | Содержание файла                            |
|-------------------------|---------------------------------------------|
| conftest.py             | Фикстуры                                    |
| curl.py                 | Файл с URL страниц                          |
| data.py                 | Файл с тестовыми данными                    |
| generator.py            | Генератор тестовых данных для пользователя  |
| stellar_burgers_api.py  | API‑клиент для сервиса Stellar Burgers      |
| requirements.txt        | Файл с зависимостями                        |
| allure_results.dir      | Папка с отчетами Allure                     |
| tests dir               | Директория с тестами                        |
| test_user.py            | Тесты создания пользователя                 |
| test_auth_user.py       | Тесты авторизации пользователя              |
| test_order.py           | Тесты создания заказа                       |