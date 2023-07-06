"""
Creating json and .txt in right path
"""


import os
import json

from src.topic_descriptor.topic_descriptor import TopicDescriptor


class MakeMetadata:
    def __init__(self, descr: TopicDescriptor):
        self.__descr = descr
        self.__file_name = f'{descr.bot_name}_{descr.command}'
        self.__metadata: dict = self.__read_template()

    def make(self):
        """Create JSON in right path"""
        md_path = os.path.join(self.__descr.output_root,
                               self.__descr.bot_name,
                               self.__descr.md_folder)
        md_full_name = f'{md_path}/{self.__file_name}.json'
        # Template instanceastion
        # self.__metadata["id"] = "random_num"
        self.__metadata["name"] = f'/{self.__descr.command}'
        self.__metadata["service_id"] = self.__descr.bot_name
        # "simple/postman_help.txt"
        self.__metadata["content"] = (
            f'{self.__metadata.get("type")}/{self.__file_name}.txt')
        try:
            os.makedirs(md_path, exist_ok=True)
            with open(md_full_name, "w") as json_file:
                json.dump(self.__metadata, json_file, indent="\t")
                print("JSON-file created:", md_full_name)
        except FileExistsError:
            print("Directory have already exist:", md_path)

    def __read_template(self) -> dict:
        with open("./src/make_topic_files/md_template.json") as read_file:
            template = json.load(read_file)
        return template
