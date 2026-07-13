import json

class GameDataHandler:
    @staticmethod
    def load_data(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_data(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def update_data(file_path, key, value):
        data = GameDataHandler.load_data(file_path)
        data[key] = value
        GameDataHandler.save_data(file_path, data)

    @staticmethod
    def delete_data(file_path, key):
        data = GameDataHandler.load_data(file_path)
        if key in data:
            del data[key]
        GameDataHandler.save_data(file_path, data)