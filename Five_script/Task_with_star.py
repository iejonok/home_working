# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    """
    Функция преобразуют арабское число в римское.
    :param val:
    :return: roman_str
    """
    # Здесь нужно написать код
    roman_numerals = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    roman_str = ''
    if val > 1000:
        num_m = val // 1000
        roman_str += roman_numerals[1000] * num_m
        val %= 1000
    if val > 100:
        num_c = val // 100
        if num_c == 9:
            roman_str += 'CM'
        elif num_c >= 5:
            roman_str += 'D' + 'C' * (num_c - 5)
        elif num_c == 4:
            roman_str += 'CD'
        else:
            roman_str += 'C' * num_c
        val %= 100
    if val > 10:
        num_x = val // 10
        if num_x == 9:
            roman_str += 'XC'
        elif num_x >= 5:
            roman_str += 'L' + 'X' * (num_x - 5)
        elif num_x == 4:
            roman_str += 'XL'
        else:
            roman_str += 'X' * num_x
        val %= 10
    if val > 0:
        if val == 9:
            roman_str += 'IX'
        elif val >= 5:
            roman_str += 'V' + 'I' * (val - 5)
        elif val == 4:
            roman_str += 'IV'
        else:
            roman_str += 'I' * val
    return roman_str


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']

for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
