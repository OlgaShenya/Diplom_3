# Автотесты Stellar Burgers

UI-автотесты для сайта [Stellar Burgers](https://qa-stellarburgers.education-services.ru/)
на Python + Selenium с использованием паттерна Page Object. Тесты запускаются
в двух браузерах — Chrome и Firefox.

## Структура проекта

```
.
├── conftest.py          # фикстуры pytest (драйвер, тестовые данные)
├── requirements.txt     # зависимости
├── locators/            # локаторы элементов по страницам
├── pages/               # Page Object классы
│   └── base_page.py     # базовый класс с обёртками над ожиданиями Selenium
└── tests/               # тесты по страницам
```

## Установка

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Драйверы Chrome и Firefox скачиваются автоматически через `webdriver-manager`.

## Учётные данные

Логин и пароль тестового пользователя берутся из переменных окружения
`STELLAR_EMAIL` и `STELLAR_PASSWORD` (если они не заданы — используются значения
по умолчанию из `conftest.py`):

```bash
# Windows (PowerShell)
$env:STELLAR_EMAIL="user@example.com"; $env:STELLAR_PASSWORD="secret"
# macOS/Linux
export STELLAR_EMAIL="user@example.com" STELLAR_PASSWORD="secret"
```

## Запуск тестов

```bash
# все тесты (в Chrome и Firefox)
pytest -v

# один файл
pytest tests/test_feed_page.py -v

# один тест
pytest tests/test_feed_page.py::TestFeedPage::test_user_orders_appear_in_feed -v
```

## Allure-отчёт
Тесты размечены шагами (`@allure.step` в Page Object) и заголовками
(`@allure.title`/`@allure.description` в тестах).
```bash
# прогнать тесты и собрать результаты
pytest --alluredir=allure-results

# открыть отчёт (нужен установленный Allure CLI)
allure serve allure-results
```
Allure CLI ставится отдельно (например, `scoop install allure` на Windows
или `brew install allure` на macOS).
## Что покрыто тестами

- Главная страница: переходы по разделам, модалка ингредиента, счётчик ингредиента, оформление заказа.
- Вход: подсветка поля пароля при показе/скрытии.
- Восстановление пароля: переход со страницы входа, отправка email.
- Личный кабинет: переход в профиль и историю заказов, выход из аккаунта.
- Лента заказов: открытие деталей заказа, появление нового заказа в ленте и в разделе «В работе», рост счётчиков выполненных заказов.
