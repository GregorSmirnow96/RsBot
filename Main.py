import time
from Bot import Bot
from KeyUtilities import KeyUtilities as Keys
from SequenceFileLoader import SequenceFileLoader

'''
time.sleep(2)
bot = SequenceFileLoader.load_sequence_from_file("C:/bot sequences/crafting sequence.txt")
bot.execute_sequence()
'''

bot = Bot.create_sequence()
# bot.save_sequence_to_file("C:/bot sequences/crafting sequence.txt")
bot.execute_sequence()
