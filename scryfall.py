import requests
import json
import os
import datetime


class ScryfallDatabase:
    def __init__(self, file_path='scryfall_data.json'):
        self.file_path = file_path
        self.data = None
        self.data_loaded = False
        self.load_database()

    def update_database(self):
        response = requests.get('https://api.scryfall.com/bulk-data')
        data = response.json()
        latest_update_link = data['data'][0]['download_uri']

        response = requests.get(latest_update_link)
        self.data = response.json()

        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)

        self.data_loaded = True

    def load_database(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
                self.data_loaded = True
        elif self.is_database_outdated():
            self.update_database()

    def is_database_outdated(self):
        if os.path.exists(self.file_path):
            file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(self.file_path))
            current_time = datetime.datetime.now()
            time_difference = current_time - file_modified_time
            return time_difference.days > 30
        return True

    def search_card_by_name(self, card_name):
        if not self.data_loaded:
            self.load_database()

        if not self.data_loaded:
            return None

        for card in self.data:
            if card['name'].lower() == card_name.lower():
                return card

        return None
