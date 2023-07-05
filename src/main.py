"""
This is a simple uttility for bot-farm project.
    1. Get alias name
    2. Create dir for new bot.
    3. Into this dir create datatopics dir
    4. Into dir datatopics create json with metadata
    5. Into dir datatopics create dir simple and create 2 files (start/help)
    6. Ask about special topics
"""


from creating_path.creating_path import CreatingPath


def main():
    """Call all classes"""
    pth = CreatingPath()
    pth.get_input()
    pth.path()


if __name__ == "__main__":
    main()
