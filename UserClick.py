import win32api, win32con
from HumanizedSleeper import HumanizedSleeper
from MouseInfo import MouseInfo

class UserClick:

    def from_text(text_representation):
        '''
        from_text is a required method for any class that is to be
        used as an IBotAction.

        The text_representation format is as follows:
            UserClick {x_coordinate} {y_coordinate} {pre_click_duration}
        '''
        components = text_representation.split()
        x_coordinate = int(components[1])
        y_coordinate = int(components[2])
        pre_click_duration = float(components[3])
        return UserClick(
            (x_coordinate, y_coordinate),
            pre_click_duration)

    def __init__(self,
        clicked_coordinate,
        pre_click_duration):
            self.clicked_coordinate = clicked_coordinate
            self.pre_click_duration = pre_click_duration
            self.sleeper = HumanizedSleeper(0.0, 0.3, 6.27)
            self.mouse_info = MouseInfo()

    def perform_action(self):
        '''
        perform_action is a required method for any class that is to
        be used as an IBotAction.
        '''
        pre_click_cursor_location = win32api.GetCursorPos()
        if (self.pre_click_duration > 0):
            self.sleeper.sleep_with_variance(self.pre_click_duration)
        self.click()
        # win32api.SetCursorPos(pre_click_cursor_location)

    def to_text(self):
        '''
        to_text is a required method for any class that is to be used
        as an IBotAction.

        The expected string output format is as follows:
            UserClick {x_coordinate} {y_coordinate} {pre_click_duration}
        '''
        return self.__class__.__name__ + " " + \
            str(self.clicked_coordinate[0]) + " " + \
            str(self.clicked_coordinate[1]) + " " + \
            str(self.pre_click_duration)
    
    def click(self):
        win32api.SetCursorPos(self.clicked_coordinate)
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTDOWN,
            self.clicked_coordinate[0],
            self.clicked_coordinate[1],
            0,
            0)
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTUP,
            self.clicked_coordinate[0],
            self.clicked_coordinate[1],
            0,
            0)