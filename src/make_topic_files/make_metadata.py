"""
Creating json and .txt in right path
"""


import os
import json

from src.topic_descriptor.topic_descriptor import TopicDescriptor


class MakeMetadata:
    def __init__(self, descr: TopicDescriptor, file_name: str):
        self.__descr = descr
        self.__file_name = file_name
        self.__metadata: dict = {"name": "/start"}

    def make(self):
        """Create JSON in right path"""
        md_path = os.path.join(self.__descr.output_root,
                               self.__descr.bot_name,
                               self.__descr.md_folder)
        md_full_name = f'{md_path}/{self.__file_name}.json'
        try:
            os.makedirs(md_path, exist_ok=True)
            with open(md_full_name, "w") as json_file:
                json.dump(self.__metadata, json_file)
                print("JSON-file created:", md_full_name)
        except FileExistsError:
            print("Directory have already exist:", md_path)
