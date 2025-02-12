import cv2
import pyautogui
import numpy as np
import time

def match_image_using_features(snippet_path, threshold=0.75):
    time.sleep(2)

    # Load the snippet image
    snippet = cv2.imread(snippet_path, cv2.IMREAD_GRAYSCALE)

    # Capture the screen
    screen = pyautogui.screenshot()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)  # Convert to BGR format
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Detect keypoints and descriptors in both the snippet and the screen
    kp_snippet, des_snippet = orb.detectAndCompute(snippet, None)
    kp_screen, des_screen = orb.detectAndCompute(gray_screen, None)

    # Use BFMatcher (Brute Force Matcher) to find the best matches
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors between snippet and screen
    matches = bf.match(des_snippet, des_screen)

    # Sort matches by distance (lower distance is better)
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw the first few matches (for visualization)
    matched_img = cv2.drawMatches(snippet, kp_snippet, screen, kp_screen, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Filter good matches based on the distance threshold
    good_matches = [m for m in matches if m.distance < threshold]

    print(f"Found {len(good_matches)} good matches")

    # If there are enough good matches, calculate the perspective transform
    if len(good_matches) > 10:
        # Extract the matched keypoints
        snippet_pts = np.float32([kp_snippet[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        screen_pts = np.float32([kp_screen[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        # Find the homography (transformation matrix) to map snippet to screen
        matrix, mask = cv2.findHomography(snippet_pts, screen_pts, cv2.RANSAC, 5.0)

        # Get the dimensions of the snippet
        h, w = snippet.shape

        # Get the coordinates of the corners of the snippet
        snippet_corners = np.float32([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]]).reshape(-1, 1, 2)

        # Project the corners to the screen using the homography
        screen_corners = cv2.perspectiveTransform(snippet_corners, matrix)

        # Draw the bounding box around the matched region
        screen = cv2.polylines(screen, [np.int32(screen_corners)], True, (0, 255, 0), 2)

        # Show the final result (optional)
        cv2.imshow("Matched Image", screen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return screen_corners
    else:
        print("Not enough good matches found.")
        return None

# Example usage
snippet_image_path = 'image_ref\\hinzufuegen.JPG'
match_image_using_features(snippet_image_path, threshold=10)
