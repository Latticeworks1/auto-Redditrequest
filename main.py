import pyautogui
import time
from pydirectinput import keyDown, keyUp

# Constants
STEAL_COLOR = (0, 232, 0)
SEARCH_REGION = (200, 250, 1920, 1080)
KEY_TO_PRESS = 'd'
SCAN_FREQUENCY = 0.05

def search_for_color(color_rgb, tolerance=5, region=None):
    """
    Search for a given color within a specified region of the screen.

    Args:
        color_rgb (tuple): The RGB color tuple to search for.
        tolerance (int, optional): Allowed variance in color. Defaults to 5.
        region (tuple, optional): The region of the screen to search (x, y, width, height).

    Returns:
        bool: True if color is found, False otherwise.
    """
    try:
        screenshot = pyautogui.screenshot(region=region)
        return any(
            all(abs(pixel_color[i] - color_rgb[i]) <= tolerance for i in range(3))
            for y in range(screenshot.height)
            for x in range(screenshot.width)
            for pixel_color in [screenshot.getpixel((x, y))]
        )
    except Exception as e:
        print(f"Error in search_for_color: {e}")
        return False

def press_key(key, press_time=0.1):
    """
    Simulate a key press for a specified duration.

    Args:
        key (str): The key to press.
        press_time (float, optional): Duration to hold the key down. Defaults to 0.1 seconds.
    """
    try:
        keyDown(key)
        time.sleep(press_time)
        keyUp(key)
    except Exception as e:
        print(f"Error in press_key: {e}")

def main():
    try:
        while True:
            if search_for_color(STEAL_COLOR, region=SEARCH_REGION):
                press_key(KEY_TO_PRESS)
            time.sleep(SCAN_FREQUENCY)
    except KeyboardInterrupt:
        print("Script terminated by user.")
    except Exception as e:
        print(f"Script terminated with an error: {e}")

if __name__ == "__main__":
    main()
