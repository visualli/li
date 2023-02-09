import cv2
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def MedianFilter(img,k,padding=None):
    imarray=img
    height = imarray.shape[0]
    width = imarray.shape[1]
    print('height=',height,width)
    if not padding:
        edge = int((k - 1) / 2)
        if height - 1 - edge <= edge or width - 1 - edge <= edge:
            print("The parameter k is to large.")
            return None
        new_arr = np.zeros((height, width), dtype="uint8")
        for i in range(edge,height-edge):
            for j in range(edge,width-edge):
                new_arr[i, j] = np.median(imarray[i - edge:i + edge + 1, j - edge:j + edge + 1])# 调用np.median求取中值
    return new_arr


img = cv2.imread(r"D:\Desktop\b.png", cv2.IMREAD_GRAYSCALE)
result1 = MedianFilter(img,3)
result2 = MedianFilter(img,5)
cv2.imwrite(r"D:\Desktop\input.jpg", img)
cv2.imwrite(r"D:\Desktop\output.png", result1)
median3 = cv2.medianBlur(img, 3)
cv2.imshow("input", img)
cv2.imshow("output", result1)
cv2.imshow("Median3", median3)
cv2.waitKey(0)
cv2.destroyAllWindows()

