import cv2
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#识别红色
def recognize_red(hsv):
    lower_red1 = np.array([0,43,46])
    upper_red1 = np.array([10,255,255])
    block1 = cv2.inRange(hsv,lower_red1,upper_red1)
    lower_red2 = np.array([156,43,46])
    upper_red2 = np.array([180,255,255])
    block2 = cv2.inRange(hsv,lower_red2,upper_red2)
    block = cv2.add(block1,block2)
    return block

#识别蓝色
def recognize_blue(hsv):
    lower_blue = np.array([100,43,46])
    upper_blue = np.array([124,255,255])
    block_blue = cv2.inRange(hsv,lower_blue,upper_blue)
    return block_blue

#形态学——腐蚀膨胀
def erosion_dilate(img):
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations = 3)
    cv2.imshow("erosion", erosion)
    dilate = cv2.dilate(erosion, kernel, iterations = 2)
    cv2.imshow("dilate", dilate)
    return dilate

# 轮廓检测，画出线条的轮廓并标出中心点
def cv_findcontours(origin_img,img):
    draw_cnt = origin_img.copy()
    cnts, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(draw_cnt, cnts, -1, (0, 255, 0), 2)
    cv_show("draw_cnt",draw_cnt)
    # 循环处理每条轮廓
    for c in cnts:
        M = cv2.moments(c)
        center_x = int(M['m10'] / M['m00'])
        center_y = int(M['m01'] / M['m00'])
        print('center_x:', center_x, 'center_y:', center_y)
        draw_cnt = draw_cnt.copy()
        cv2.circle(draw_cnt, (center_x, center_y), 7, (255,255,255), -1)  # 绘制中心点
        str1 = '(' + str(center_x) + ',' + str(center_y) + ')'  # 把坐标转化为字符串
        cv2.putText(draw_cnt, str1, (center_x - 50, center_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2,cv2.LINE_AA)  # 绘制坐标点位
        cv_show('draw_cnt', draw_cnt)


img = cv2.imread(r"D:\Desktop\a.png")
cv2.imshow("img", img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rec_red = recognize_red(hsv)
rec_blue = recognize_blue(hsv)
cv2.imshow("rec_red", rec_red)
#cv2.imshow("rec_blue", rec_blue)
rec_red_median = cv2.medianBlur(rec_red,3)
rec_blue_median = cv2.medianBlur(rec_blue,3)
cv_show("rec_red_median", rec_red_median)
#cv_show("rec_blue_median", rec_blue_median)
dilate = erosion_dilate(rec_red_median)
cv_findcontours(img, dilate)


