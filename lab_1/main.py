from work_with_files import *
from encrypt_text_with_key import *
from frequency_analysis import *
from merge_key import *
from create_caesar_key import *


if __name__ == "__main__":
    
    constants = load_json_file('constants.json')

    alphabet = constants['alphabet']
    shift = constants['shift']
    key1 = constants['key1']
    text1 = constants['text1']
    encrypted_text = constants['encrypted_text']
    cipher = constants['cipher']
    unsecret_text = constants['unsecret_text']
    key2 = constants['key2']
    probabilities = constants['probabilities']
    ru = constants['ru']
    
    create_caesar_key(shift, key1, alphabet)
    encrypt_text_with_key(text1, key1, encrypted_text)
    frequency_analysis(cipher, probabilities)
    merge_key(ru, probabilities, key2)
    encrypt_text_with_key(cipher, key2, unsecret_text)