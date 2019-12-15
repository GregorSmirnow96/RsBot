from ClickSequenceCreator import ClickSequenceCreator
from KeyUtilities import KeyUtilities as Keys

class Bot:

    def create_sequence():
        bot = Bot()
        bot.initialize_sequence()
        return bot

    def __init__(self):
        self.click_sequence_creator = None

    def set_sequence_creator(self, sequence_creator):
        self.click_sequence_creator = ClickSequenceCreator()

    def initialize_sequence(self):
        self.action_sequence = self.clickSequenceCreator.create_click_sequence()

    def execute_sequence(self):
        if (self.action_sequence == None):
            pass
        while (not self.terminate_sequence()):
            self.action_sequence.get_next_action().perform_action()

    def terminate_sequence(self):
        return Keys.key_was_pressed(Keys.ESCAPE)
    
    def save_sequence_to_file(self, file_path):
        sequence_file = open(file_path, "w+")
        for action in self.action_sequence:
            sequence_file.write(action.to_text() + "\n")
