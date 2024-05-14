import json

def encrypt_text_with_dict(text_file_path, dict_file_path, output_file_path):
    
    with open(text_file_path, "r", encoding="utf-8") as text_file:
        text = text_file.read()
        
    with open(dict_file_path, "r", encoding="utf-8") as dict_file:
        dictionary = json.load(dict_file)
        
    encrypted_text = ""
    for char in text:
        if char in dictionary:
            encrypted_text += dictionary[char]
        else:
            encrypted_text += char
            
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(encrypted_text)
    return encrypted_text