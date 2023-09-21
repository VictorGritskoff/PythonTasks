# Пример программы с использованием try\except\finally

try:
    x = int(input("Введите число: "))
    result = 10 / x
    print("Результат: ", result)
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print("Деление на ноль невозможно")
finally:
    print("Программа завершена")