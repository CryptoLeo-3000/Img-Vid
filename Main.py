import cv2
import glob

images = glob.glob("*.jpg")

for im in images:
    img = cv2.imread(im, 0)
    resize = cv2.resize(img, (1920, 1080))
    cv2.imshow("Hey", resize)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.imwrite(f"{im}_resize", resize)