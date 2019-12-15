from Bot import Bot
from UserClick import UserClick

class SequenceFileLoader:

    action_factory_method = {
        UserClick.__name__: UserClick.from_text
    }

    def load_sequence_from_file(file_path):
        sequence_file = open(file_path, "r")
        file_lines = sequence_file.readlines()
        actions = []
        for line in file_lines:
            action_type = line.split()[0]
            action_factory_function = SequenceFileLoader.action_factory_methods[action_type]
            next_action = action_factory_function(line)
            actions.append(next_action)

        bot = Bot()
        bot.action_sequence = actions
        return bot
