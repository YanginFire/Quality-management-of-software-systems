import shutil  # библиотека для операций над файлами и директориями
import os

def directory_work():  # работа с директориями
    print("1 - Создать директорию" + "\n" + "2 - Удалить директорию")
    choise = int(input())
    if choise == 1:
        print("Введите полный путь до директории:" + '\n')
        name = str(input())
        if "file manager testing" not in name:
            print("Нельзя работать вне папки file manager testing ")
        else:
            os.mkdir(name)
    if choise == 2:
        print("Введите полный путь до папки:" + '\n')
        name = str(input())
        if "file manager testing" not in name:
            print("Нельзя работать вне папки file manager testing")
        else:
            os.rmdir(name)


def file_work():  # работа с файлами
    print("Введите полный путь до файла:")
    choise = str(input())
    if "file manager testing" not in choise:
        print("Нельзя работать вне папки file manager testing")
    else:
        print(
            "1 - Создать файл" + "\n" + "2 - Удалить файл" + "\n" + "3 - Читать файл" + "\n" + "4 - Запись в файл" + "\n" + "5 - Переименовывание" + "\n" + "6 - Копирование")
        mark = int(input())
        if mark == 1:
            file = open(choise, 'a+')
            file.close()
        elif mark == 2:
            os.remove(choise)
        elif mark == 3:
            with open(choise) as file:
                for line in file:
                    print(line)
        elif mark == 4:
            print("Введите строку для записи:")
            phrase = str(input())
            file = open(choise, 'a+')
            file.write(phrase)
            file.close()
        elif mark == 5:
            print("Введите новое название (полный путь)")
            mark3 = str(input())
            os.rename(choise, mark3)
        elif mark == 6:
            print("Введите новый путь (полный)")
            mark3 = str(input())
            shutil.copyfile(choise, mark3)


while True:  # бесконечный цикл обработки запросов
    print(
        "1 - Создать/удалить директорию" + '\n' + "2 - Создать/удалить файл/Работа с файлом")
    ans = int(input())
    if ans == 1:
        directory_work()
    elif ans == 3:
        file_work()