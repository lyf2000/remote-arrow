import socket

import pyautogui


class ArrowControlAdapter:
    """Adapter for phone actions and send to PC."""

    @classmethod
    def click_keyb(cls, action: str):
        pyautogui.press([action])


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(("10.254.254.254", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP
