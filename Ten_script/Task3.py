# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("input_data, expected_output", [
    ((8, 2), 4),
    ((8, 0), ZeroDivisionError),
    pytest.param((-15, 3), -5, marks=pytest.mark.skip(reason="Тест пропущен")),
    pytest.param((-8, -2), 4, marks=pytest.mark.smoke)
    ], ids=['positive_test', 'Zero', 'negative_test', 'smoke'])
def test_all_division(input_data, expected_output):
    if input_data[1] == 0:
        with pytest.raises(ZeroDivisionError):
            all_division(input_data[0], input_data[1])
    else:
        assert all_division(*input_data) == expected_output
