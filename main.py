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


def make_command_list():
    """"""
    command_list = ["start", "help"]
    new_commands = input("New commands(separate by comma): ").strip()
    if len(new_commands) > 0:
        if "," in new_commands:
            new_commands_list = new_commands.split(",")
        else:
            new_commands_list = [new_commands]
        command_list = [*command_list, *new_commands_list]
    return command_list


def make_topic_files(cmd_list, dscr):
    """"""
    for cmd in cmd_list:
        dscr.command = cmd.strip()
        md_maker = MakeMetadata(dscr)
        md_maker.make()
        cn_maker = MakeContent(dscr)
        cn_maker.make()


def main():
    """Main flow"""
    bot_name = input("Print bot-name alias: ").strip()
    dscr = TopicDescriptor(bot_name)
    ft_maker = MakeFolderTree(dscr)
    ft_maker.make()
    cmd_list = make_command_list()
    m_t_files = make_topic_files(cmd_list, dscr)
    

if __name__ == "__main__":
    main()
