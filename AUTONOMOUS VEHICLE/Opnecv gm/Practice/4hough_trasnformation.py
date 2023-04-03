import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from img_disp import mult_disp as show





original = cv.imread((r"C:\Users\risha\OneDrive\Desktop\Opnecv gm\Practice\room.jpg"))

original = cv.resize(original,(500,400), interpolation= cv.INTER_LINEAR)
gray = cv.cvtColor(original,cv.COLOR_BGR2GRAY)
# CANNY
edges = cv.Canny(gray,200,300)


blur = cv.GaussianBlur(edges,(5,5),0)
# HOUGHLINESP
lines= cv.HoughLinesP(blur,1,np.pi/180,100,minLineLength=200,maxLineGap=30)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(original,(x1,y1),(x2,y2),(0,255,0),2)


show(original,gray,edges,width=500,height=350)

# plt.subplot(221,figsize=(6,6)),plt.imshow(original,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# plt.subplot(222),plt.imshow(gray,cmap = 'gray')
# plt.title('Gray Image'), plt.xticks([]), plt.yticks([])

# plt.subplot(223),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


