import time
from MouseInfo import MouseInfo
from KeyUtilities import KeyUtilities as Keys
from UserClick import UserClick

class ClickSequenceCreator:

    def __init__(self):
        self.user_clicks = []
        self.initial_previous_click_time = -1
        self.previous_click_time = self.initial_previous_click_time
        self.current_click_time = 0

    def create_click_sequence(self):
        mouse_info = MouseInfo()
        finding_click_locations = True
        while (finding_click_locations):
            if (mouse_info.user_left_clicked()):
                coordinate_clicked = mouse_info.get_cursor_location()
                user_click = UserClick(coordinate_clicked, self.get_click_interval())
                self.user_clicks.append(user_click)
            finding_click_locations = not Keys.key_was_pressed(Keys.SHIFT)
        self.user_clicks[0].pre_click_duration = self.get_click_interval()
        return self.user_clicks
    
    def get_click_interval(self):
        self.current_click_time = time.time()
        if (self.previous_click_time == self.initial_previous_click_time):
            click_interval = 0
        else:
            click_interval = self.current_click_time - self.previous_click_time
        self.previous_click_time = self.current_click_time
        return click_interval
