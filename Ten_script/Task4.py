# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import datetime


@pytest.fixture(scope='class')
def time_class_fixture(request):
    start_time = datetime.datetime.now()
    request.cls.start_time = start_time
    yield
    end_time = datetime.datetime.now()
    duration = end_time - request.cls.start_time
    print(f"\nВремя начала выполнения тестов: {request.cls.start_time}")
    print(f"Время окончания выполнения тестов: {end_time}")
    print(f'Продолжительность выполнения тестов: {duration}')


@pytest.mark.usefixtures("setup_fixture", "time_class_fixture")
class TestClass:

    def test_one(self, test_time):
        assert 1 == 1

    def test_two(self, test_time):
        assert 2 == 2


def test_three(test_time):
    assert 3 == 3


def test_four(setup_fixture, test_time):
    assert 4 == 4
