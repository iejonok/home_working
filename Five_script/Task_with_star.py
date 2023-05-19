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

    roman_str = ''
    num = [1000, 500, 100, 50, 10, 5, 1]
    rom = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    i = 0
    while val > 0:
        for plug in range(val // num[i]):
            roman_str += rom[i]
            val -= num[i]
        i += 1
    roman_str = roman_str.replace('DCCCC', 'CM')
    roman_str = roman_str.replace('CCCC', 'CD')
    roman_str = roman_str.replace('LXXXX', 'XC')
    roman_str = roman_str.replace('XXXX', 'XL')
    roman_str = roman_str.replace('VIIII', 'IX')
    roman_str = roman_str.replace('IIII', 'IV')
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
