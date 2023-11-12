# Задача 1

grocery_list = input("Напишіть продукти (5 або більше), які потрібно купити, використовуйте пробіл як роздільник: ").split()

if len(grocery_list) >= 5:
    # Відображає список доданих продуктів.
    print(f"Зараз у кошику такі продукти: {str(grocery_list).strip('[]')}")
    product_all_removal_flag = input('Бажаєте видалити з корзини деякі продукти? (Д/Н):')
    product_all_removal_flag = product_all_removal_flag.lower()

    if product_all_removal_flag == 'д':
        # Бажаєте видалити з корзини деякі продукти? - Да
        # Видалення 1
        product_number = input(f"Видалення 1. Вкажіть порядковий номер продукту, який потрібно видалити (от 1 до {len(grocery_list)}): ")
        grocery_list.pop(int(product_number) - 1)
        print(f"Зараз у кошику такі продукти: {str(grocery_list).strip('[]')}")

        # Видалення 2
        product_number = input(f"Видалення 2. Вкажіть порядковий номер продукту, який потрібно видалити (от 1 до {len(grocery_list)}): ")
        grocery_list.pop(int(product_number) - 1)
        print(f"Зараз у кошику такі продукти: {str(grocery_list).strip('[]')}")

        # Видалення 3
        product_number = input(f"Видалення 3. Вкажіть порядковий номер продукту, який потрібно видалити (от 1 до {len(grocery_list)}): ")
        grocery_list.pop(int(product_number) - 1)
        print(f"Зараз у кошику такі продукти: {str(grocery_list).strip('[]')}")

        # Видалення 4
        product_number = input(f"Видалення 4. Вкажіть порядковий номер продукту, який потрібно видалити (от 1 до {len(grocery_list)}): ")
        grocery_list.pop(int(product_number) - 1)
        print(f"Зараз у кошику такі продукти: {str(grocery_list).strip('[]')}")

        # Видалення 5
        product_number = input(f"Видалення 5. Вкажіть порядковий номер продукту, який потрібно видалити (от 1 до {len(grocery_list)}): ")
        grocery_list.pop(int(product_number) - 1)

        # Перевірка порожній кошик чи ні після видалення.
        if len(grocery_list) == 0:
            # Порожній кошик після видалення, додайте продукти.
            add_list = input("Кошик порожній, додайте продукти, використовуйте пробіл як роздільник: ").split()
            grocery_list = grocery_list + add_list
            print(f"У кошику тепер є такі продукти: {str(grocery_list).strip('[]')}\nДо побачення!")
        else:
            # Не порожній кошик після видалення, до побачення.
            print(f"У кошику є такі продукти: {str(grocery_list).strip('[]')}\nДо побачення!")

    else:
        # Бажаєте видалити з корзини деякі продукти? - Ні:
        print(f"У кошику є такі продукти: {str(grocery_list).strip('[]')}\nДо побачення!")

else:
    # Було додано менше 5 продуктів.
    print("Додано менше 5 продуктів.\nДо побачення!")