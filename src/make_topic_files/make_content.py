"""

"""


import os
from src.topic_descriptor.topic_descriptor import TopicDescriptor


class MakeContent():
    def __init__(self, descr: TopicDescriptor, file_name: str):
        self.__descr = descr
        self.__file_name = file_name
        self.__content: str = "Hello, User!"

    def make(self):
        """Create content in right path"""
        cn_path = os.path.join(self.__descr.output_root,
                               self.__descr.bot_name,
                               self.__descr.md_folder,
                               self.__descr.cn_folder)
        cn_full_name = f'{cn_path}/{self.__file_name}.txt'
        try:
            os.makedirs(cn_path, exist_ok=True)
            with open(cn_full_name, "w") as content_file:
                content_file.write(self.__content)
                print("Content-file created:", cn_full_name)
        except FileNotFoundError:
            print("Directory have already exist:", cn_path)
