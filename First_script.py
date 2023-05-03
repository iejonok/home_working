# 1. Квадрат.
side = 5  # сторона квадрата
square = side ** 2  # площадь квадрата
perimeter = side * 4  # периметр квадрата
diagonal = (2 * square) ** 0.5  # диагональ квадрата
print('Площадь квадрата равна: ', square)
print('Периметр квадрата равен: ', perimeter)
print('Диагональ квадрата равна: ', diagonal)
print('\n')

# 2. Квадратное уравнение.
print('Решаем уравнение: a*x²+b*x+c=0')  # квадратное уравнение
a = 1  # первый коэффициент
print('a=', a)
b = 2  # второй коэффициент
print('b=', b)
c = 3  # свободный член
print('c=', c)
D = b ** 2 - 4 * a * c  # дискриминант
print('Дискриминант равен: ', D)
if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)  # первый корень уравнения
    x2 = (-b - D ** 0.5) / (2 * a)  # второй корень уравнения
    print('Первый корень равен: ', round(x1, 2))
    print('Второй корень равен: ', round(x2, 2))
if D < 0:
    print('Решения нет')
if D == 0:
    x1 = -b / (2 * a)
    print('Корень один и равен: ', round(x1, 2))
print('\n')

# 3. Объединение строк. Замена символов между строками.
string1 = 'Первая строка с текстом.'
string2 = 'Вторая строка с цифрами.'
print(string1, string2)
symbol12_string1 = string2[:2]  # первые два символа первой строки.
symbol12_string2 = string1[:2]  # первые два символа второй строки.
print(symbol12_string1 + string1[2:], symbol12_string2 + string2[2:])  # Меняем символы между строками.
print(f'{string2[:2]}{string1[2:]} {string1[:2]}{string2[2:]}')  # Решение этой задачи без дополнительных переменных.
print('\n')

# 4. Операции с путём до файла.
string = r'D:\na.kostylev\ВО\2.52\Sbis1C_UF.epf'  # исходный путь до файла
# длина строки print(len(string))
print(f'Имя файла без расширения: {string[23:-4]}\nДиск: {string[:3]}\nКорневая папка: {string[:14]}\n')
print('\n')

# 5. Числа строками
a = 2  # число один
print('a=:', a)
b = 6  # число два
c = a + b  # сумма
c1 = a * b  # произведение
print('b=:', b)
print(f'{a} + {b} = {c}\n{a} * {b} = {c1}')
print('\n')

# 6. Удаление символов с нечётными значениями индексов.
string1 = 'Очередная строка с текстом.'  # исходная строка
string2 = string1[::2]  # удаление символов с нечётными значениями индексов в исходной строке
print(string2)
print('\n')

# 7. Срез.
string1 = 'wtf'
print('Первая строка:', string1)
string2 = 'brick quz jmpy veldt whangs fox'
print('Вторая строка:', string2)
string3 = string2.find('w'), string2.find('t'), string2.find('f')  # поиск индексов символов из первой строки
string4 = min(string3)  # минимальный индекс
string5 = max(string3) + 1  # максимальный индекс
print(f'Минимальный срез второй строки по символам из первой: {string2[string4:string5]}')  # срез
