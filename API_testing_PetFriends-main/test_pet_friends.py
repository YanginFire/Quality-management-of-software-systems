import os

from api import PetFriends
from variables_with_valid_data import valid_email, valid_password
from variables_with_invalid_data import invalid_email,invalid_password

pet_f = PetFriends()

# вхождение с валидными данными для получение ключа - passed
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pet_f.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result

# вхождение с невалидными данными для получение ключа - passed
def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    status, result = pet_f.get_api_key(invalid_email, invalid_password)
    assert status == 403


# вхождение валидным паролем и невалидной почтой для получение ключа - passed
def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    status, result = pet_f.get_api_key(invalid_email, valid_password)
    assert status == 403

# вхождение валидной почтой и невалидным паролем для получение ключа - passed
def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    status, result = pet_f.get_api_key(valid_email, invalid_password)
    assert status == 403

# вхождение с валидными данными для получение ключа и получение списка животных через ключ
# Список животных пуст
def test_get_all_pets_by_valid_key(filter=""):
    _, auth_key = pet_f.get_api_key(valid_email, valid_password)
    status, result = pet_f.get_lists_of_pets_by_auth_key(auth_key,filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_post_create_pet_with_novalid_key(name="Мурка", animal_type="Кошка", age=3):
    auth_key = {"key": '8a417540fe39eae66f0bcdbafd453e1fadfc2bf1b50cbc0d634b1fa1'}

    status, result = pet_f.post_create_pet(auth_key,name,animal_type,age)
    assert status == 403

def test_post_new_pet_with_valid_data_novalid_key(name='Vasya', animal_type='Dvornyaga',age='2', pet_photo='images\jpeg\cat.jpg'):
    auth_key = {"key": '8a417540fe39eae66f0bcdbafd453e1fadfc2bf1b50cbc0d634b1fa1'}
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pet_f.post_add_pet(auth_key,name,animal_type,age,pet_photo)
    assert status == 400

def test_post_new_pet_with_null_data(name='', animal_type='',age='', pet_photo='images\jpeg\cat.jpg'):
    _, auth_key = pet_f.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pet_f.post_add_pet(auth_key, name, animal_type, age,pet_photo)
    assert status == 400

def test_delete_pet_with_valid_data_novalid_key(pet_id=0):
    auth_key = {"key": '8a417540fe39eae66f0bcdbafd453e1fadfc2bf1b50cbc0d634b1fa1'}
    status, _ = pet_f.delete_pet(auth_key,pet_id)
    assert status == 403

def test_put_pet_with_valid_data_novalid_key(pet_id='0',name='Мурзик1',animal_type='Кот', age=1):
    auth_key = {"key": '8a417540fe39eae66f0bcdbafd453e1fadfc2bf1b50cbc0d634b1fa1'}
    status, result = pet_f.put_pet(auth_key,pet_id,name,animal_type,age)
    assert status == 403

