# Sprint_5 - UI Автотесты для сервиса "Доска"

## Описание
Проект содержит UI-автотесты для учебного сервиса "Доска" с использованием Selenium.

## Требования
- Python 3.7+
- Google Chrome
- ChromeDriver

## Установка
1. Установить зависимости:
`pip install selenium pytest`

2. Установите ChromeDriver, соответствующий вашей версии Chrome

## Запуск тестов
`pytest -v`

## Структура проекта
- `locators/` - локаторы элементов
- `tests/` - тестовые сценарии
- `conftest.py` - фикстуры
- `README.md` - описание проекта

## Команды для запуска

# Запуск всех тестов
`pytest -v`

# Запуск конкретного файла
`pytest tests/test_registration.py -v`

# Запуск с отчётом о прохождении
`pytest -v --tb=short`

# Запуск в несколько потоков (если установлен pytest-xdist)
`pytest -n 4 -v`