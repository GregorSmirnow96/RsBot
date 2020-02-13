from ClickSequenceCreator import ClickSequenceCreator
from KeyUtilities import KeyUtilities as Keys

class Bot:

    def __init__(self):
        self.clickSequenceCreator = ClickSequenceCreator()

    def initialize_sequence(self):
        self.action_sequence = self.clickSequenceCreator.create_click_sequence()

    def execute_sequence(self):
        while (True):
            for action in self.action_sequence:
                if (self.terminate_sequence()):
                    break
                action.perform_action()

    def terminate_sequence(self):
        return Keys.key_was_pressed(Keys.ESCAPE)
    
    def save_sequence_to_file(self, file_path):
        sequence_file = open(file_path, "w+")
        for action in self.action_sequence:
            sequence_file.write(action.to_text() + "\n")