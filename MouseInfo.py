import win32gui
from KeyUtilities import KeyUtilities as Keys

class MouseInfo:

    def __init__(self):
        self.left_mouse_button_was_pressed = False

    def user_left_clicked(self):
        left_click_was_pressed = False
        if (not self.left_mouse_button_was_pressed):
            left_click_was_pressed = Keys.key_was_pressed(Keys.LEFT_MOUSE_BUTTON)
        self.left_mouse_button_was_pressed = Keys.key_was_pressed(Keys.LEFT_MOUSE_BUTTON)
        return left_click_was_pressed

    def get_cursor_location(self):
        return win32gui.GetCursorInfo()[2]