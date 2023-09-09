
# Дано натуральное число, напишите программу, которая определяет
# является ли последовательность его цифр при просмотре
# справа налево упорядоченной по возрастанию

print("Вариант 6 задание 1")

def is_ordered(num):
    digits = [int(d) for d in str(num)]
    if digits == sorted(digits):
        return True
    else:
        return False

    if not digits:
        return False

while True:
    try:
        num = int(input("Введите натуральное число от 1 до 99999: "))
        if num <= 0 or num >= 100000:
            raise ValueError
        break
    except ValueError:
        print("Некорректный ввод. Введите натуральное число от 1 до 99999.")

if is_ordered(num):
    print("Последовательность цифр упорядочена по возрастанию")
else:
    print("Последовательность цифр не упорядочена по возрастанию")


