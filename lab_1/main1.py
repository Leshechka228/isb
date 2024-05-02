import json

# Функция для шифрования текста с использованием словаря
def encrypt_text_with_dict(text, dictionary):
    encrypted_text = ""
    for char in text:
        if char in dictionary:
            encrypted_text += dictionary[char]
        else:
            encrypted_text += char
    return encrypted_text

# Загрузка словаря из JSON файла
def load_dict_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Получение пути к JSON файлу с словарем и к исходному текстовому файлу
dict_file_path = "C:\\Users\\User\\Desktop\\oib\\isb\\lab_1\\task 1\\key1.json"
text_file_path = "C:\\Users\\User\\Desktop\\oib\\isb\\lab_1\\task 1\\text.txt"
encrypted_text_file_path = "C:\\Users\\User\\Desktop\\oib\\isb\\lab_1\\task 1\\encrypted_tex.txt"

# Загрузка словаря
dictionary = load_dict_from_json(dict_file_path)

# Чтение исходного текста
with open(text_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Шифрование текста с использованием словаря
encrypted_text = encrypt_text_with_dict(text, dictionary)

with open(encrypted_text_file_path, 'w', encoding='utf-8') as file:
    file.write(encrypted_text)
