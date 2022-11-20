<<<<<<< HEAD
def start_training(char_name, char_class):

    # Transfer character description to JSON
    path_to_person = os.path.join(os.path.dirname(__file__), 'person.txt')
    path_to_welcome = os.path.join(os.path.dirname(__file__), 'welcome.txt')
    with open(path_to_person) as f:
        info_person = json.loads(f.read())
    print(char_class == info_person)

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
=======
# coding: utf-8
import json
import os

choice_class = os.path.join(os.path.dirname(__file__), 'choice_class.txt')
with open(choice_class) as f:
     
     info = json.loads(f.read())

print(info['warrior'])
>>>>>>> d568a2c1e99a655e05fa95aaec28ac107e2282b7
