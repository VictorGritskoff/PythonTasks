# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу
# Считается, что любые два элемента, равные друг другу образуют одну пару
# которую необходимо посчитать


nums_list = []
while True:
    user_input = input("Введите числа через пробел: ")
    try:
        nums_list = [int(num) for num in user_input.split()]
        break
    except ValueError:
        print("Ошибка: введите только целые числа, разделенные пробелом.")

pairs = 0

for i in range(len(nums_list)):
    for j in range(i + 1, len(nums_list)):
        if nums_list[i] == nums_list[j]:
            pairs += 1

print(f"Количество пар элементов, равных друг другу: {pairs}")