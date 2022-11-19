# coding: utf-8
import json
import os
from random import randint


def attack(char_name, char_class):
    comment = 'нанёс урон противнику равный '
    if char_class == 'warrior':
        return (f'{char_name} {comment} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {comment} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} {comment} {5 + randint(-3, -1)}')


def defence(char_name, char_class):
    defence = ['блокировал', 'урона']
    if char_class == 'warrior':
        return (f'{char_name} {defence[0]} {10 + randint(5, 10)} {defence[1]}')
    if char_class == 'mage':
        return (f'{char_name} {defence[0]} {10 + randint(-2, 2)} {defence[1]}')
    if char_class == 'healer':
        return (f'{char_name} {defence[0]} {10 + randint(2, 5)} {defence[1]}')


def special(char_name, char_class):
    special_info = ['применил специальное умение']
    if char_class == 'warrior':
        return (f'{char_name} {special_info[0]} "Выносливость" {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} {special_info[0]} Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} {special_info[0]} Защита {10 + 30}»')


def start_training(char_name, char_class):

    # Transfer character description to JSON
    path_to_person = os.path.join(os.path.dirname(__file__), 'person.txt')
    path_to_welcome = os.path.join(os.path.dirname(__file__), 'welcome.txt')
    with open(path_to_person) as f:
        info_person = json.loads(f.read())
    print(info_person[char_class])
    with open(path_to_welcome) as f:
        print(f.read())
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    choice_class = os.path.join(os.path.dirname(__file__), 'choice_class.txt')
    with open(choice_class) as f:
        info = json.loads(f.read())
    while approve_choice != 'y':
        char_class = input(info['char_class'])
        print(info.get(char_class, 'Нет такого персонажа'))
        approve_choice = input(info['approve_choice']).lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
