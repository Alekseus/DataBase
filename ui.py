from get_push_data import get_data
from add_data import add_data


def operations():
    print('\n1 - Информацию об учениках \n2 - Добавляем ученика\n3 - Выход из программы\n')
    a = input('Выберите действие: ')

    while True:
        if a == '1':
            print(*get_data())
            operations()
        if a == '2':
            add_data()
            operations()
        if a == '3':
            print('Спасибо за сеанс, работа закончена.')
            exit()