import os

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Файл '{file_path}' успешно удален.")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")