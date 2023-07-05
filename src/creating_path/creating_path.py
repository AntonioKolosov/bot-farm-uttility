"""
Creating path package
"""


import os

from input_alias.input_alias import InputAlias


class CreatingPath():
    def __init__(self) -> None:
        self.path_name: str = ""

    def path(self):
        """Creating path"""
        # Get current dir
        current_directory = os.getcwd()
        # Create new dir with right path
        path = os.path.join(current_directory,
                            "../bot-farm-topics",
                            self.path_name, "datatopics/simple")
        try:
            os.makedirs(path)
            print("Folder %s created!" % path)
        except FileExistsError:
            print("Folder %s already exists" % path)

    def get_input(self):
        """Take input"""
        # Creating an instance of class
        als = InputAlias("Initial Alias")
        # Input alias from user
        self.path_name = als.input()
