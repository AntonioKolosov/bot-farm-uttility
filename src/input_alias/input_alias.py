"""
Input alias class
"""


class InputAlias():
    def __init__(self, alias) -> None:
        self._alias: str = alias

    def input(self):
        """Input alias"""
        return input("Print your alias: ").strip()
