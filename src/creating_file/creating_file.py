"""
Creating json and .txt in right path
"""


import os
import json


class JSONCreator:
    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.metadata = None

    def create_json(self, directory_name, filename, data):
        """Create JSON in right path"""
        # Path for creating JSON
        directory_path = os.path.join(self.base_directory,
                                      directory_name,
                                      "datatopics")
        json_path = os.path.join(directory_path, filename)

        try:
            os.makedirs(directory_path, exist_ok=True)

            with open(json_path, "w") as json_file:
                json.dump(data, json_file)
                print("JSON-file created:", json_path)
        except FileExistsError:
            print("Directory have already exist:", directory_path)
