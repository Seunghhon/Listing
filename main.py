import json
from pprint import pprint

def load_json(filename='info.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json(new_data, filename='info.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data["person"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4, ensure_ascii=False)
        print("Successfully added data to file.")

name = input("Enter name: ")
age = int(input("Enter age: "))
address = input("Enter address: ")

new_json_object = {
    '이름': name,
    '나이': age,
    '동네': address
}

write_json(new_json_object)
updated_data = load_json()
pprint(updated_data)
    

