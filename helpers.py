"""Вспомогательные функции для тестов"""

import random
import string

def generate_test_email():
    """Генерация уникального email для каждого теста"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{random_string}@test.com"