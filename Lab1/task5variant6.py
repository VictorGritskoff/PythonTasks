# Словарь с товарами
products = {
    "Книга": [100, 10], # цена и количество
    "Ручка": [20, 50],
    "Тетрадь": [50, 20],
    "Карандаш": [10, 100],
    "Альбом": [150, 5]
}

# Функция для просмотра цены товара
def view_price(product):
    if product in products:
        price = products[product][0]
        print(f"{product}: {price} руб.")
        print("\n\n")
    else:
        print("Товар не найден")
        print("\n\n")

# Функция для просмотра количества товара
def view_quantity(product):
    if product in products:
        quantity = products[product][1]
        print(f"{product}: {quantity} шт.")
    else:
        print("Товар не найден")

# Функция для просмотра всей информации о товарах
def view_all():
    for product in products:
        price = products[product][0]
        quantity = products[product][1]
        print(f"{product}: {price} руб. - {quantity} шт.")

# Функция для покупки товара
def buy_product(product, quantity):
    if product in products:
        if quantity <= products[product][1]:
            price = products[product][0] * quantity
            products[product][1] -= quantity
            print("\n\n")
            print(f"Вы купили {quantity} шт. товара '{product}' за {price} руб.")
            print(f"Осталось {products[product][1]} шт.")
            print("\n\n")
        else:
            print("Недостаточно товара на складе")
            print("\n\n")
    else:
        print("Товар не найден")
        print("\n\n")

# Главный цикл программы
while True:
    print("\n\n")
    print("1. Просмотр цены")
    print("2. Просмотр количества")
    print("3. Вся информация")
    print("4. Покупка")
    print("5. До свидания")
    print("\n\n")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        product = input("Введите название товара: ")
        view_price(product)
    elif choice == "2":
        product = input("Введите название товара: ")
        view_quantity(product)
    elif choice == "3":
        view_all()
    elif choice == "4":
        product = input("Введите название товара: ")
        if product == "n":
            break
        while True:
            try:
                quantity = int(input("Введите количество: "))
                break
            except ValueError:
                print("Проверьте свой ввод!")
        buy_product(product, quantity)
    elif choice == "5":
        break
    else:
        print("Неверный выбор")