from constants import *
from encrypt_text_with_dict import *
from frequency_analysis import *
from merge_dicts import *

if __name__ == "__main__":
    encrypt_text_with_dict(text1, key1, encrypted_text)
    frequency_analysis(cipher, probabilities)
    merge_dicts(ru, probabilities, key2)
    encrypt_text_with_dict(cipher, key2, unsecret_text)