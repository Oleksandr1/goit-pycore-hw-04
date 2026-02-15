# Завдання 1

# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. 
# Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

# Наприклад:
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000

# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну 
# та середню суму заробітної плати всіх розробників.

import sys


def total_salary(path):
    with open(path, "r") as file:
        total = 0
        count = 0
        for line in file:
            name, salary = line.strip().split(",")
            total += int(salary)
            count += 1
        
    average = total / count if count > 0 else 0
    return total, average



# Завдання 2

# У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:

# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5

# Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.



# Вимоги до завдання:
    
# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
# Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

def get_cats_info(path):
    cats_info = []
    with open(path, "r") as file:
        for line in file:
            cat_id, name, age = line.strip().split(",")
            cats_info.append({"id": cat_id, "name": name, "age": int(age)})
    return cats_info


# Завдання 3

# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і 
# візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. 
# Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися
#  за кольором.


# Вимоги до завдання:

# Створіть віртуальне оточення Python для ізоляції залежностей проекту.
# Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
# Використання бібліотеки colorama для реалізації кольорового виведення.
# Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
# Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.

from colorama import Fore, Style
import os
import sys

def visualize_directory_structure(path, indent=0):
    if not os.path.exists(path):
        print(f"{Fore.RED}Error: Такого шляху не існує.{Style.RESET_ALL}")
        return
    if not os.path.isdir(path):
        print(f"{Fore.RED}Error: Вказаний шлях не є директорією.{Style.RESET_ALL}")
        return

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"{' ' * indent}{Fore.BLUE}{item}/ {Style.RESET_ALL}")
            visualize_directory_structure(item_path, indent + 4)
        else:
            print(f"{' ' * indent}{Fore.GREEN}{item} {Style.RESET_ALL}")
    



def parse_input(user_input):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Error: Contact '{name}' not found."

def show_phone(args, contacts):
    if not args:
        return "Error: Enter user name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Error: Contact '{name}' not found."

def show_all(contacts):
    if not contacts:
        return "Contact list is empty."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if(__name__ == "__main__"):
    # # tast 1
    # uncomment the code below to test the functions for task 1

    # total, average = total_salary("salaries.txt")
    # print(f"Total Salary: {total}")
    # print(f"Average Salary: {average}")

    # # task 2
    # uncomment the code below to test the functions for and task 2


    # cats_info = get_cats_info("cats_data.txt")
    # print("Cats Info:")
    # for cat in cats_info:
    #     print(cat)
    
    # uncomment the code below to test the function for task 3
    
    # visualize_directory_structure(sys.argv[1])

    main()

