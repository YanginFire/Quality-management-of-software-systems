# Тестирование API сайта PetFriends

# Задание 3 

Методические указание:
IDE: VS Code, Pycharm, Replit
Язык: Python
Библиотека Requests
Фрейворк: Pytest
# Задание:
Зарегистрироваться: https://petfriends1.herokuapp.com
Ознакомиться с документацией API: https://petfriends1.herokuapp.com/apidocs/#/
Написать приложение содержащие функции работы с API реализовать методы:

    GET, 
    POST, 
    PUT, 
    DELETE
    
Написать тесты для функций работы с API

    Тесты должны содержать позитивные и негативные сценарии
    Необходимо сделать параметризацию
    Необходимо использовать фикстуры 
    
Запустить  тесты и сделать скриншот
Создаем файл README.md, с описанием приложения
Загружаем файлы на Github


В данной работе опубликованно несколько важных файлов

    api.py
    test_pet_friend.py
    variable_with_invalid_data.py
    variable_with_valid_data.py
    
В файле api.py описаны функции работы с API сайта
Получение ключа пользователя по email и password
![image](https://user-images.githubusercontent.com/90453727/147415892-4da502af-012c-4220-9c70-3aeb9a763750.png)
Вывод списка животных которые добавлял пользователь
![image](https://user-images.githubusercontent.com/90453727/147415899-31132a8b-71cf-4a53-97b1-959f8c70c2d6.png)
Добавление новой информации о питомце
![image](https://user-images.githubusercontent.com/90453727/147415906-3cd35d7f-c54d-4fd9-b8bd-123e706c8f19.png)
Добавление информации о животном без фотографии
![image](https://user-images.githubusercontent.com/90453727/147415919-b9c2a674-2c1e-4eb1-9972-9e6afd8010bb.png)
Удаление животного
![image](https://user-images.githubusercontent.com/90453727/147415935-5246d01b-1557-43d2-af3f-325011d7c130.png)
Добавление доп информации по животному
![image](https://user-images.githubusercontent.com/90453727/147415945-87204ee0-d4b0-497c-a9a0-c9164d78c117.png)

В файле test_pet_friend.py описаны 10 тестов для тестирования работаспособности функций API
![image](https://user-images.githubusercontent.com/90453727/147415971-221bf06a-ddd2-466b-9345-d4fa57481dd3.png)
![image](https://user-images.githubusercontent.com/90453727/147415975-0f8f3ffc-8c6d-4639-bf81-d981b4c8fafe.png)
![image](https://user-images.githubusercontent.com/90453727/147415980-60b870e0-674f-4af7-88f2-d383910b0ffe.png)

В файлах variable_with_invalid_data.py и variable_with_valid_data.py описаны данные которые понадобяться для тестирования получения ключа пользователя и вход с валидными и не валидными данными

Проверим работjспособность программы для тестирования с помощью библиотек requests и pytest
![image](https://user-images.githubusercontent.com/90453727/147416197-5888477c-3dce-4057-8bcc-4f3d9d3d1737.png)


