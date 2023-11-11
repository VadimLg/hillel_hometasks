# Задача 1
grocery_list = []
message_add = 'Добавьте продукт'
message_current = 'Сейчас в корзине следующие продукты:\n'
message_removal = 'Хотите удалить продукт'
message_order_is_processed = 'Заказ оформлен. До свидания! Спасибо за сотрудничесво!'
message_incorrect_answer = 'Был введен некорретный ответ, нужно вводить (Y/N)"'

print('Добавьте в корзину 5 продуктов')

current_product = input(message_add + ' 1: ')
grocery_list.append(current_product)

current_product = input(message_add + ' 2: ')
grocery_list.append(current_product)

current_product = input(message_add + ' 3: ')
grocery_list.append(current_product)

current_product = input(message_add + ' 4: ')
grocery_list.append(current_product)

current_product = input(message_add + ' 5: ')
grocery_list.append(current_product)

# Отображение списка добавленных продуктов.
print(message_current, '1.', grocery_list[0], '\n2.', grocery_list[1], '\n3.', grocery_list[2], '\n4.', grocery_list[3],
      '\n5.', grocery_list[4], sep='')

product_all_removal_flag = input('Хотите удалить из корзины некоторые продукты? (Y/N):')
product_all_removal_flag = product_all_removal_flag.lower()

if product_all_removal_flag == 'y' or product_all_removal_flag == 'yes':

    product_removal_flag = input(message_removal + ' 1? (Y/N)')
    product_removal_flag = product_removal_flag.lower()
    if product_removal_flag == 'y' or product_removal_flag == 'yes':
        grocery_list[0] = ''
        # Отображение списка после удаления продукта.
        print(message_current, '1.', grocery_list[0], '\n2.', grocery_list[1], '\n3.', grocery_list[2], '\n4.',
              grocery_list[3],
              '\n5.', grocery_list[4], sep='')
    elif product_removal_flag != 'n' or product_removal_flag == 'no':
        print(message_incorrect_answer)

    product_removal_flag = input(message_removal + ' 2? (Y/N)')
    product_removal_flag = product_removal_flag.lower()
    if product_removal_flag == 'y' or product_removal_flag == 'yes':
        grocery_list[1] = ''
        # Отображение списка после удаления продукта.
        print(message_current, '1.', grocery_list[0], '\n2.', grocery_list[1], '\n3.', grocery_list[2], '\n4.',
              grocery_list[3],
              '\n5.', grocery_list[4], sep='')
    elif product_removal_flag != 'n' or product_removal_flag == 'no':
        print(message_incorrect_answer)

    product_removal_flag = input(message_removal + ' 3? (Y/N)')
    product_removal_flag = product_removal_flag.lower()
    if product_removal_flag == 'y' or product_removal_flag == 'yes':
        grocery_list[2] = ''
        # Отображение списка после удаления продукта.
        print(message_current, '1.', grocery_list[0], '\n2.', grocery_list[1], '\n3.', grocery_list[2], '\n4.',
              grocery_list[3],
              '\n5.', grocery_list[4], sep='')
    elif product_removal_flag != 'n' or product_removal_flag == 'no':
        print(message_incorrect_answer)

    product_removal_flag = input(message_removal + ' 4? (Y/N)')
    product_removal_flag = product_removal_flag.lower()
    if product_removal_flag == 'y' or product_removal_flag == 'yes':
        grocery_list[3] = ''
        # Отображение списка после удаления продукта.
        print(message_current, '1.', grocery_list[0], '\n2.', grocery_list[1], '\n3.', grocery_list[2], '\n4.',
              grocery_list[3],
              '\n5.', grocery_list[4], sep='')
    elif product_removal_flag != 'n' or product_removal_flag == 'no':
        print(message_incorrect_answer)

    product_removal_flag = input(message_removal + ' 5? (Y/N)')
    product_removal_flag = product_removal_flag.lower()
    if product_removal_flag == 'y' or product_removal_flag == 'yes':
        grocery_list[4] = ''
        # Отображение списка после удаления продукта.
        print(message_current, '1.', grocery_list[0], '\n2.', grocery_list[1], '\n3.', grocery_list[2], '\n4.',
              grocery_list[3],
              '\n5.', grocery_list[4], sep='')
    elif product_removal_flag != 'n' or product_removal_flag == 'no':
        print(message_incorrect_answer)

    # Проверка есть ли продукты в списке после 5 запросов на удаление продуктов.
    if grocery_list[0] == '' and grocery_list[1] == '' and grocery_list[2] == '' and grocery_list[3] == '' and \
            grocery_list[4] == '':
        print('Список пустой, пожалуйста добавьте продукты.')

        current_product = input(message_add + ' 1: ')
        grocery_list[0] = current_product

        current_product = input(message_add + ' 2: ')
        grocery_list[1] = current_product

        current_product = input(message_add + ' 3: ')
        grocery_list[2] = current_product

        current_product = input(message_add + ' 4: ')
        grocery_list[3] = current_product

        current_product = input(message_add + ' 5: ')
        grocery_list[4] = current_product

        # Отображение списка снова добавленных продуктов
        print(message_current, '1.', grocery_list[0], '\n2.', grocery_list[1], '\n3.', grocery_list[2], '\n4.',
              grocery_list[3],'\n5.', grocery_list[4], sep='')
        # Отображаем что заказ оформлен (после повторного добавления продуктов если список был пустой)
        print(message_order_is_processed)
    else:
        # Отображаем что заказ оформлен (когда список не был пустым после удаления некоторых продуктов)
        print(message_order_is_processed)

elif product_all_removal_flag == 'n' or product_all_removal_flag == 'no':
    # Отбражаем когда был введен ответ "N" на вопрос 'Хотите удалить из корзины некоторые продукты? (Y/N):'
    print(message_order_is_processed)
else:
    # Отбражаем когда был введен некорректный ответ на вопрос 'Хотите удалить из корзины некоторые продукты? (Y/N):'
    print(message_incorrect_answer)