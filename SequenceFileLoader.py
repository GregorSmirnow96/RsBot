from Bot import Bot
from UserClick import UserClick

class SequenceFileLoader:

    action_factory_methods = \
    {
        UserClick.__name__: UserClick.from_text
    }

    def load_sequence_from_file(file_path):
        sequence_file = open(file_path, "r")
        file_lines = sequence_file.readlines()
        actions = []
        for line in file_lines:
            action_type = line.split()[0]
            next_action = SequenceFileLoader.action_factory_methods[action_type](line)
            actions.append(next_action)

        bot = Bot()
        bot.action_sequence = actions
        return bot
