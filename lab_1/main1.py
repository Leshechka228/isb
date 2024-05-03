import os
import json
from collections import Counter
from constants import *
from encrypt_text_with_dict import *

def load_dict_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def frequency_analysis(input_file_path: str, output_file_path: str) -> None:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n', '')  # Убираем символы переноса строки из текста
    print(text)

    total_chars = len(text)

    frequencies = {}
    for char in text:
        if char != '\n':  # Игнорируем символы переноса строки
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1

    probabilities = {char: count / total_chars for char, count in frequencies.items()}

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(probabilities, output_file, ensure_ascii=False, indent=4)



if __name__ == "main":
    dictionary = load_dict_from_json(dict_file_path)

    with open(text_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    encrypted_text = encrypt_text_with_dict(text, dictionary)

    with open(encrypted_text_file_path, 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

    text_path = "C:\\Users\\User\\Desktop\\oib\\isb\\lab_1\\task 2\\cipher.txt"
    output_path = "C:\\Users\\User\\Desktop\\oib\\isb\\lab_1\\task 2\\frequency_analysis.json"
    with open(cipher, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n', '')  # Убираем символы переноса строки из текста
    print(text)
    frequency_analysis(text_path, output_path)