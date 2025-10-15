import os
from PIL import Image
import cv2

path = str(input("Path: "))

jpglist = []

for dir, fldrs, files in os.walk(path):
    fullPaths = [os.path.join(dir, file) for file in files]
    for i in fullPaths:
        split = os.path.splitext(i)
        if split[1] == '.jpg':
            jpglist.append(i)

img_files = jpglist

for file in img_files:
    image = cv2.imread(file)
    img = Image.open(file)
    width, height = img.size
    image = cv2.resize(image, (width,height))

    cv2.namedWindow("Photos", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Photos", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Photos", image)

    cv2.waitKey(2000)

cv2.waitKey(2000)
cv2.destroyAllWindows()