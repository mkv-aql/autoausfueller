import cv2
import numpy as np
import mss
import time
import pyautogui

width = 1920
height = 1080

# Set the screen area to capture
monitor = {"top": 0, "left": 0, "width": width, "height": height}

# Create a VideoCapture object for recording
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_recording.avi", fourcc, 20.0, (1920, 1080))

# Create an MSS instance for screen capture
time.sleep(2)
with mss.mss() as sct:
    print("Recording starts")
    while True:
        # Capture a screenshot
        screenshot = sct.grab(monitor)

        # Convert the screenshot to a format OpenCV can work with (BGR)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)


        # Get the current mouse position
        mouse_x, mouse_y = pyautogui.position()

        # Draw the mouse cursor (a small circle for simplicity)
        # You can use a more complex cursor image or shape if desired
        cursor_radius = 10
        cv2.circle(img, (mouse_x, mouse_y), cursor_radius, (0, 0, 255), -1)  # Red cursor

        # Write the frame to the video file
        out.write(img)

        # Display the screen capture (optional)
        # cv2.imshow("Screen Recorder with Mouse", img)

        # Stop recording if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release everything when done
out.release()
cv2.destroyAllWindows()
