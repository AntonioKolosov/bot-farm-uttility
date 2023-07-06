"""
Creating path package
"""


import os
import shutil

from src.topic_descriptor.topic_descriptor import TopicDescriptor


class MakeFolderTree():
    def __init__(self, descr: TopicDescriptor) -> None:
        self.__descr = descr

    def make(self) -> None:
        """Creating path"""
        # Get current dir
        current_directory: str = os.getcwd()
        # Create new dir with right path
        path: str = os.path.join(current_directory,
                                 self.__descr.output_root,
                                 self.__descr.bot_name,
                                 self.__descr.md_folder,
                                 self.__descr.cn_folder)
        try:
            os.makedirs(path)
            print("Folder %s created!" % path)
        except FileExistsError:
            print("Folder %s already exists" % path)
            re_create = input("Press Y/y to continue re-create path or N/n"
                              "to add new files to the existing directory: ")
            if re_create.lower() == "y":
                shutil.rmtree(path)
                os.makedirs(path)
                print("Folder %s re-created!" % path)
            else:
                print("Files will be added to the existing directory.")
