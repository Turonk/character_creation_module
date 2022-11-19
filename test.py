# coding: utf-8
import json
import os

choice_class = os.path.join(os.path.dirname(__file__), 'choice_class.txt')
with open(choice_class) as f:
     
     info = json.loads(f.read())

print(info['warrior'])