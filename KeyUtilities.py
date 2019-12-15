import win32api

class KeyUtilities:

    LEFT_MOUSE_BUTTON = 0x01
    SHIFT = 0x10
    ESCAPE = 0x1B
    SPACE = 0x20

    def key_was_pressed(key_id):
        return win32api.GetKeyState(key_id) < 0

    def wait_for_key_to_be_pressed(key_id):
        key_was_pressed = False
        while (not key_was_pressed):
            key_was_pressed = KeyUtilities.key_was_pressed(KeyUtilities.SPACE)