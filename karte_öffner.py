import cv2

# directory = 'C:\\Users\\AgamSafaruddinDeutsc\\Pictures\\erfurter str.png'
directory = 'C:\\Users\\AgamSafaruddinDeutsc\\Pictures\\Magdeburgerstrasse.png'
window_name = '59192 Bergkamen Weddinghofen Magdeburger Straße'
img = cv2.imread(directory)

#Keep image window on top
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
# keep window on top
cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
cv2.resizeWindow(window_name, 800, 800)

cv2.imshow(window_name, img)
cv2.waitKey(0)

cv2.destroyAllWindows()