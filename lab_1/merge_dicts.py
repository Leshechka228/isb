import json
from delete_file import *

def merge_dicts(json_path1, json_path2, output_json_path):
    merged_dict = {}
    
    with open(json_path1, 'r', encoding='utf-8') as file1:
        dict1 = json.load(file1)
    
    with open(json_path2, 'r', encoding='utf-8') as file2:
        dict2 = json.load(file2)
    
    keys1 = list(dict2.keys())
    keys2 = list(dict1.keys())

    for i in range(len(keys1)):
        if i < len(keys2):
            merged_dict[keys1[i]] = keys2[i]
    
    with open(output_json_path, 'w', encoding='utf-8') as outfile:
        json.dump(merged_dict, outfile, ensure_ascii=False, indent=4)
        
    delete_file(json_path2)