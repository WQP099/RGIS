import numpy as np
import cv2
from use_sqlite import sqlitefun

#
panoramic_bin = sqlitefun.sqlite_select_imagebin("20200205_123003_533219", "panoramic")[0][0]
imagepath = "localImage.jpg"
with open(imagepath, 'wb') as f:
        f.write(panoramic_bin)
img = cv2.imread("localImage.jpg")
pos_list = ["211,1659","2682,2671"]#x,y
wh = "168,27"#w,h
panel_w = int(wh.split(',')[0])
panel_h = int(wh.split(',')[1])
for pos in pos_list:
    pos_x = int(pos.split(',')[0])
    pos_y = int(pos.split(',')[1])
    Lift_X = int(pos_x-(panel_w/2))
    Lift_Y = int(pos_y-(panel_h/2))
    Right_X = int(pos_x+(panel_w/2))
    Right_Y = int(pos_y+(panel_h/2))
    img = cv2.rectangle(img, (Lift_X, Lift_Y), (Right_X, Right_Y), (0, 255, 0), -1)
# img = cv2.rectangle(img,(124,1645),(295,1673),(0,255,0),-1)
# img = cv2.rectangle(img,(124,1645),(295,1673),(0,255,0),-1)
#cv2.imshow('img3',img)
cv2.imwrite('localImage1.jpg',img)
# cv2.waitKey(0)
# cv2.destroyWindow()