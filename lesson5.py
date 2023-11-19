# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно). (так як робили на уроці).
# Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
#
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити (додавання, віднімання, множення, ділення).
# і виведіть йому цю табличку.

dict_tabl = {}
list_multiplication = []
list_addition = []
list_dividing = []
list_difference = []
list_result = []

for i in range(2, 10):
    for j in range(2, 10):
        list_multiplication.append(str(i) + '*' + str(j) + '=' + str(i * j))
        list_addition.append(str(i) + '+' + str(j) + '=' + str(i + j))
        list_dividing.append(str(i) + '/' + str(j) + '=' + str(i / j))
        list_difference.append(str(i) + '-' + str(j) + '=' + str(i - j))
dict_tabl['*'] = list_multiplication
dict_tabl['+'] = list_addition
dict_tabl['/'] = list_dividing
dict_tabl['-'] = list_difference

print('Яку табличку ви хочете побачити?')
table_switch = input('Для вибору додавання введіть "+", для віднімання введіть "-", для множення введіть "*", для ділення введіть "-": ')

if table_switch == '+':
    list_result = dict_tabl['+']
elif table_switch == '-':
    list_result = dict_tabl['-']
elif table_switch == '*':
    list_result = dict_tabl['*']
elif table_switch == '/':
    list_result = dict_tabl['/']

print('Результат:')
print(', '.join(list_result))