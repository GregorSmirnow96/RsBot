import time
from Mouse import Mouse
from KeyUtilities import KeyUtilities as Keys
from UserClick import UserClick

class ClickSequenceCreator:

    def __init__(self):
        self.user_clicks = []
        self.previous_click_time = None
        self.current_click_time = 0
        self.listening_for_user_clicks = True
        self.mouse = Mouse()

    def create_click_sequence(self):
        finding_click_locations = True
        while finding_click_locations:
            self.listen_for_clicks()
        self.user_clicks[0].pre_click_duration = self.get_time_since_previous_click()
        return self.user_clicks
    
    def listen_for_click(self):
        if self.mouse.user_left_clicked():
            cursor_location = mouse.get_cursor_location()
            time_since_previous_click = self.get_time_since_previous_click()
            user_click = UserClick(
                cursor_location = cursor_location,
                pre_click_duration = time_since_previous_click)
            self.user_clicks.append(user_click)
        self.listening_for_user_clicks = not Keys.key_was_pressed(Keys.SHIFT)
        
    def get_time_since_previous_click(self):
        self.current_click_time = time.time()
        if self.previous_click_time:
            time_since_previous_click = self.current_click_time - self.previous_click_time
        else:
            time_since_previous_click = 0
        self.previous_click_time = self.current_click_time
        return time_since_previous_click
