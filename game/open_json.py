import json

def get_data():
    with open('file.json', 'r', encoding='utf-8') as f: 
        tic_tac_toe = json.load(f) 
        return tic_tac_toe