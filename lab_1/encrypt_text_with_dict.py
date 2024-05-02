def encrypt_text_with_dict(text, dictionary):
    encrypted_text = ""
    for char in text:
        if char in dictionary:
            encrypted_text += dictionary[char]
        else:
            encrypted_text += char
    return encrypted_text