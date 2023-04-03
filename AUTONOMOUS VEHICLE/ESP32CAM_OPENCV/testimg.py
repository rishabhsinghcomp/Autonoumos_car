import cv2 as cv
import numpy as np
import sys
sys.path.append(r"C:\Users\risha\OneDrive\Desktop\AUTONOMOUS VEHICLE\Opnecv gm\Practice")
from img_disp import mult_disp



img = cv.imread(r"C:\Users\risha\OneDrive\Desktop\AUTONOMOUS VEHICLE\ESP32CAM_OPENCV\t.png")
img_gray=cv.imread(r"C:\Users\risha\OneDrive\Desktop\AUTONOMOUS VEHICLE\ESP32CAM_OPENCV\t.png",0)





m1 = np.zeros_like(img)
m2= np.zeros_like(img_gray)



# vertices = np.array([[0,600],[0,200],[800,200],[800,600]])
vertices = np.array([[0,600],[0,300],[200,200],[600,200],[800,300],[800,600]])


cv.fillPoly(m1,np.int32([vertices]),(255))





mult_disp(m1,img,width=500,height=500)


cv.waitKey(0)
