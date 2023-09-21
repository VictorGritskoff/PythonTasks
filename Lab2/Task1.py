#  Написать функцию is_prime, принимающую 1 аргумент — число от 0
#  до 1000, и возвращающую True, если оно простое, и False - иначе.

def is_prime(number):
    if not isinstance(number, int) or number < 0 or number > 1000:
        raise ValueError("Аргумент должен быть целым числом от 0 до 1000")
    try:
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    except TypeError:
        print("Аргумент должен быть целым числом")
    finally:
        print("Функция завершена")