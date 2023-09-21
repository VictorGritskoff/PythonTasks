# Дана строка в виде случайной последовательности чисел от 0 до 9
# Требуется создать словарь, который в качестве ключей будет
# принимать данные числа (т. е. ключи будут типом int), а в качестве
# значений – количество этих чисел в имеющейся последовательности.

def count_digits(string):
    digits = {}
    for char in string:
        if char.isdigit():
            if char in digits:
                digits[char] += 1
            else:
                digits[char] = 1
    return digits


string = input("Введите сюда вашу строку: ")
digit_count = count_digits(string)
print(digit_count)