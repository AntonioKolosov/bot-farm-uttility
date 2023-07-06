"""
This is a simple uttility for bot-farm project.
    1. Get alias name
    2. Create dir for new bot.
    3. Into this dir create datatopics dir
    4. Into dir datatopics create json with metadata
    5. Into dir datatopics create dir simple and create 2 files (start/help)
    6. Ask about special topics
"""


from src.make_folder_tree.make_folder_tree import MakeFolderTree
from src.make_topic_files.make_content import MakeContent
from src.make_topic_files.make_metadata import MakeMetadata
from src.topic_descriptor.topic_descriptor import TopicDescriptor


def main():
    """Main flow"""
    bot_name = input("Print bot-name alias: ").strip()
    dscr = TopicDescriptor(bot_name)
    ft_maker = MakeFolderTree(dscr)
    ft_maker.make()

    md_maker = MakeMetadata(dscr, f'{bot_name}_start')
    md_maker.make()

    cn_maker = MakeContent(dscr, f'{bot_name}_start')
    cn_maker.make()

if __name__ == "__main__":
    main()
