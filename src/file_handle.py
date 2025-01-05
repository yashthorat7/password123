import json

def read_json(file_name):
    with open('./data/'+ file_name, 'r') as file:
        return json.load(file)

def write_json(file_name, data):
    with open('./data/'+ file_name, 'w') as file:
        file_data = json.load(file)

def append_json(file_name, data):
    with open('./data/'+ file_name, 'a') as file:
        file_data = json.load(file)