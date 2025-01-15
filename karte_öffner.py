import cv2

directory = 'C:\\Users\\AgamSafaruddinDeutsc\\Pictures\\erfurter str.png'

img = cv2.imread(directory)

#Keep image window on top
cv2.namedWindow('59192 Bergkamen Weddinghofen', cv2.WINDOW_NORMAL)
# keep window on top
cv2.setWindowProperty('59192 Bergkamen Weddinghofen', cv2.WND_PROP_TOPMOST, 1)
cv2.resizeWindow('59192 Bergkamen Weddinghofen', 800, 800)

cv2.imshow('59192 Bergkamen Weddinghofen', img)
cv2.waitKey(0)

cv2.destroyAllWindows()