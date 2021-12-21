import os
import shutil
import pytest

const_dir_path = "/Users/katya/PycharmProjects/testing_file_manager/test"
const_file_path = "/Users/katya/PycharmProjects/testing_file_manager/test.txt"


# ФИКСТУРЫ

# Все функции файлового менеджера находятся тут, в своей отдельной фикстуре

# Создание папки
@pytest.fixture
def dir_work_1():
    if "testing_file_manager" not in const_dir_path:
        print("Нельзя работать вне папки testing_file_manager")
    else:
        os.mkdir(const_dir_path)
        return True


# Удаление папки
@pytest.fixture
def dir_work_2():
    if "testing_file_manager" not in const_dir_path:
        print("Нельзя работать вне папки testing_file_manager")
    else:
        os.rmdir(const_dir_path)
        return True


# Создание файла
@pytest.fixture
def mk_file():
    file = open(const_file_path, 'a+')
    file.close()
    return True


# Запись в файл
@pytest.fixture
def w_file():
    try:
        phrase = "Hello world"
        file = open(const_file_path, 'a+')
        file.write(phrase)
        file.close()
        return True
    except FileNotFoundError:
        print("Файл не существует")


# Чтение файла
@pytest.fixture
def r_file():
    try:
        with open(const_file_path) as file:
            for line in file:
                print(line)
        return True
    except FileNotFoundError:
        print("Файл не существует")


# Копирование файла из одной папки в другу
@pytest.fixture
def copy_file():
    try:
        print("введите новый путь (полный)")
        mark3 = "/Users/katya/PycharmProjects/testing_file_manager/text.txt"
        shutil.copyfile(const_file_path, mark3)
        return True
    except FileNotFoundError:
        print("Файл не существует")


# Переименование файла
@pytest.fixture
def rename_file():
    try:
        print("введите новое название (полный путь)")
        mark3 = "/Users/katya/PycharmProjects/testing_file_manager/test_renamed.txt"
        os.rename(const_file_path, mark3)
        return True
    except FileNotFoundError:
        print("Файл не существует")


# Перемещение файла из одной папки в другу
@pytest.fixture
def move_file():
    try:
        print("Укажите новый путь (полный)")
        mark = "/Users/katya/PycharmProjects/testing_file_manager/test_renamed.txt"
        mark3 = "/Users/katya/PycharmProjects/testing_file_manager/new_test_renamed.txt"
        shutil.copyfile(mark, mark3)
        os.remove(mark)
        return True
    except FileNotFoundError:
        print("Файл не существует")


# Удаление файла
@pytest.fixture
def del_file():
    try:
        mark3 = "/Users/katya/PycharmProjects/testing_file_manager/text.txt"
        os.remove(mark3)
        return True
    except FileNotFoundError:
        print("Файл не существует")


# ТЕСТЫ

def test_dir_work_1(dir_work_1):
    assert (dir_work_1 == 1)


def test_dir_work_2(dir_work_2):
    assert (dir_work_2 == 1)


def test_mk_file(mk_file):
    assert (mk_file == 1)


def test_w_file(w_file):
    assert (w_file == 1)


def test_r_file(r_file):
    assert (r_file == 1)


def test_copy_file(copy_file):
    assert (copy_file == 1)


def test_rename_file(rename_file):
    assert (rename_file == 1)


def test_move_file(move_file):
    assert (move_file == 1)


def test_del_file(del_file):
    assert (del_file == 1)