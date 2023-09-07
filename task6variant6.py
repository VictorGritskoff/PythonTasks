# Запрос ввода списка с клавиатуры
input_list = input("Введите список чисел через запятую: ")

# Преобразуем строку в список, исключая возможные ошибки
try:
    numbers = [int(num) for num in input_list.split(",")]
except ValueError:
    print("Ошибка: в списке присутствуют нечисловые значения")
    exit()

# Преобразуем список в множество для получения уникальных элементов
unique_numbers = set(numbers)

# Преобразуем множество обратно в список и сортируем в обратном порядке
result = tuple(sorted(list(unique_numbers), reverse=True))

print(result)