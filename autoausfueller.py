__author__ = 'mkv-aql'

import cv2
import numpy as np
import pyautogui
import time

directory = 'D:\\Users\\AGAM MUHAJIR\\Documents\\Projects\\autoausfueller'

def match_and_click(template_path, confidence=0.8):
    """
    Matches a template image within the current screen and moves the mouse to click it.

    Args:
        template_path (str): Path to the template image (snippet).
        confidence (float): Minimum confidence threshold for a match (0 to 1).
    """
    # Capture the current screen
    screenshot = pyautogui.screenshot()

    # show screenshot
    # screenshot.show()

    # Convert the screenshot to a numpy array
    screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Read the snippet image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    if template is None:
        print("Error loading the snippet image. Check the file path.")
        return

    # Match template using cv2.matchTemplate
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if match is above confidence threshold
    if max_val >= confidence:
        # Get the coordinates of the match
        top_left = max_loc
        h, w = template.shape
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2

        # Simulate mouse movement and click
        pyautogui.moveTo(center_x, center_y)
        pyautogui.click()
        print(f"Clicked at ({center_x}, {center_y}) with confidence {max_val}")
    else:
        print(f"No match found with confidence >= {confidence}")


# Example usage
if __name__ == "__main__":
    # Wait for 2 seconds before starting
    time.sleep(2)

    # Path to the snippet image
    add_image = f'{directory}\\hinzufuegen.JPG'  # Replace with your snippet image path

    # Call the function
    match_and_click(add_image)

    time.sleep(0.2)

    new_address_image = f'{directory}\\addresse_neu.JPG'  # Replace with your snippet image path

    # Call the function
    match_and_click(new_address_image)

    time.sleep(0.2)
