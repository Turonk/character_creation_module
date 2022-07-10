from random import randint


def attack(char_name, char_class):
    if char_class == 'warior':
        return (f'{char_name} нанес урон противнику равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанес урон противнику равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанес урон противнику равный {5 + randint(-3, -1)}')
def defence(char_name, char_class):
    if char_class == 'warior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
def special(char_name, char_class):
    if char_class == 'warior':
        return (f'{char_name} примернил специальное умение  - выпосливось {80 + 25}')
    if char_class == 'mage':
        return (f'{char_name} примернил специальное умение -  атака {5 + 40}')
    if char_class == 'healer':
        return (f'{char_name} примернил специальное умение - защита {10 + 30}')




def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель - отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг - превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь - чародей способный исцелять раны.')
    print('Теперь можно потренироваться в управлении полученными навыками.')
    print('Введи одну из команд: attack для проведения атаки, defence - блокирование атаки противника и special - активация специальной возможности класса.')
    print('Чтобы пропустить тренировку введите - skip')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введите команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена'

def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Для выбора класса персонажа введите его название (warrior, mage, healer): ')
        if char_class == 'warrior':
            print('Описание воителя ....')
        if char_class == 'mage':
            print('Описание мага ....')
        if char_class == 'healer':
            print('Опиание лекаря ....')
        approve_choice = input('Подтвердите (Y) или повторите (any key) выбор ').lower()
    return char_class


def main():
    print('Приветствую тебя искатель приключений!')
    print('Прежде чем войти в игру')
    char_name = input('Назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость 80, атака 5 и защита 10.')
    print('Но ты можешь выбрать один из трех путей силы.')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
    

main()