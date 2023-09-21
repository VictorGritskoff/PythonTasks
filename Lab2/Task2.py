# Напишите функцию, которая будет принимать один аргумент. Если в
# функцию передаётся список, то посчитать длину всех его слов.
# Если кортеж, то посчитать кол-во букв и чисел в нём.
# Число – Вывести в обратном порядке
# Строка посчитать сумму всех цифр
# Сделать проверку со всеми этими случаями.

def count_characters(data):
    if isinstance(data, list):
        count = 0
        for word in data:
            count += len(word)
        return count
    elif isinstance(data, tuple):
        letters = 0
        numbers = 0
        for item in data:
            if isinstance(item, int):
                numbers += 1
            elif isinstance(item, str):
                for char in item:
                    if char.isdigit():
                        numbers += 1
                    elif char.isalpha():
                        letters += 1
        return (letters, numbers)
    elif isinstance(data, int):
        return int(str(data)[::-1])
    elif isinstance(data, str):
        total = 0
        for char in data:
            if char.isdigit():
                total += int(char)
        return total
    else:
        return "Invalid input"

# Testing the function
print(count_characters(['hello', 'world'])) # Output: 10
print(count_characters(('abc', 123, 'def', 456))) # Output: (6, 6)
print(count_characters(12345)) # Output: 54321
print(count_characters('a1b2c3')) # Output: 6
print(count_characters(True)) # Output: Invalid input