from api import PetFriends
from variables_with_valid_data import valid_email, valid_password

print("GET реализация")

pet_f = PetFriends()

result = pet_f.get_api_key(valid_email,valid_password)

print(result)

print("Получаем ключ затем реализовываем функцию get_lists_of_pets_by_auth_key")

_, key = pet_f.get_api_key(valid_email,valid_password)
print(key)

pets = pet_f.get_lists_of_pets_by_auth_key(key, 'my_pets')
print(pets)
