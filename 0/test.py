import os

BASE_PATH = os.path.dirname(__file__)
TXT_FILE = os.path.join(BASE_PATH, 'Readme.txt')


with open(TXT_FILE, 'r', encoding='utf8') as file:
    print(file.read())
