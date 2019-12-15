import time
from MouseInfo import MouseInfo
from KeyUtilities import KeyUtilities as Keys
from UserClick import UserClick

class ClickSequenceCreator:

    def __init__(self):
        self.user_clicks = []
        self.previous_click_time = None
        self.current_click_time = 0

    def create_click_sequence(self):
        mouse = Mouse()
        finding_click_locations = True
        while (finding_click_locations):
            if (mouse.user_left_clicked()):
                coordinate_clicked = mouse.get_cursor_location()
                user_click = UserClick(coordinate_clicked, self.get_time_since_previous_click())
                self.user_clicks.append(user_click)
            finding_click_locations = not Keys.key_was_pressed(Keys.SHIFT)
        self.user_clicks[0].pre_click_duration = self.get_time_since_previous_click()
        return self.user_clicks
    
    def get_time_since_previous_click(self):
        self.current_click_time = time.time()
        if (self.previous_click_time):
            time_since_previous_click = self.current_click_time - self.previous_click_time
        else:
            time_since_previous_click = 0
        self.previous_click_time = self.current_click_time
        return time_since_previous_click

