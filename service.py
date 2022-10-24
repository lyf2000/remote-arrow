import pyautogui


class ArrowControlAdapter:
    """Adapter for phone actions and send to PC."""

    @classmethod
    def click_keyb(cls, action: str):
        pyautogui.hotkey("ctrl", "shift", "c")
