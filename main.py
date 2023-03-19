# EulerTask7 - 10001-е простое число

# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

# Какое число является 10001-м простым числом?

def is_simple(num):
    """
    Функция, определяющая является ли простым
    :param num: проверяемое число
    :return: True - да
    """
    fl = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            fl = False
            break
    return fl


def get_simple_number(count):
    """
    Функция, определяющая простое число по его номеру в ряду простых чисел
    :param count: номер простого числа
    :return: значение числа
    """
    cnt = 1
    num = 1
    while cnt < count + 1:
        num += 1
        if is_simple(num) is True:
            cnt += 1
    return num


print(f"6-е простое число: {get_simple_number(6)}")
print(f"10001-е простое число: {get_simple_number(10001)}")
