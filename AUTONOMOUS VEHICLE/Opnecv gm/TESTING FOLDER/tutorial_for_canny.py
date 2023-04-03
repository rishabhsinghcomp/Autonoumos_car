from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse





# img = cv.imread('TESTING FOLDER\helmate.jpg')
# img = cv.resize(img,(700,400), interpolation= cv.INTER_LINEAR)
# gry= cv.cvtColor(img,cv.COLOR_RGB2GRAY)

# canny_on_original =cv.Canny(img,threshold1=200,threshold2=300)

# # canny_on_gray =    cv.Canny(gry,threshold1=200,threshold2=300)

# cv.imshow("original",img)
# cv.imshow("canny_on_original",canny_on_original)
# # cv.imshow("canny_on_gray",canny_on_gray)


# cv.waitKey(0)
# cv.destroyAllWindows()







# OPENCV OFFICIAL TUT


# import cv2 as cv
# max_lowThreshold = 100
# window_name = 'Edge Map'
# title_trackbar = 'Min Threshold:'
# ratio = 3
# kernel_size = 3
# def CannyThreshold(val):
#     low_threshold = val
#     img_blur = cv.blur(src_gray, (3,3))
#     detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)
#     mask = detected_edges != 0
#     dst = src * (mask[:,:,None].astype(src.dtype))
#     cv.imshow(window_name, dst)
# parser = argparse.ArgumentParser(description='Code for Canny Edge Detector tutorial.')
# parser.add_argument('--input', help='Path to input image.', default='fruits.jpg')
# args = parser.parse_args()
# src = cv.imread("TESTING FOLDER\helmate.jpg")
# src = cv.resize(src,(700,400), interpolation= cv.INTER_LINEAR)

# if src is None:
#     print('Could not open or find the image: ', args.input)
#     exit(0)
# src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# cv.namedWindow(window_name)
# cv.createTrackbar(title_trackbar, window_name , 0, max_lowThreshold, CannyThreshold)
# CannyThreshold(0)
# cv.waitKey()







# stack canny tut
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

def callback(x):
    print(x)

img = cv2.imread('TESTING FOLDER\helmate.jpg', 0) #read image as grayscale
img = cv.resize(img,(700,400), interpolation= cv.INTER_LINEAR)

canny = cv2.Canny(img, 85, 255) 

cv2.namedWindow('image') # make a window with name 'image'
cv2.createTrackbar('L', 'image', 0, 255, callback) #lower threshold trackbar for window 'image
cv2.createTrackbar('U', 'image', 0, 255, callback) #upper threshold trackbar for window 'image

while(1):
    numpy_horizontal_concat = np.concatenate((img, canny), axis=1) # to display image side by side
    cv2.imshow('image', numpy_horizontal_concat)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #escape key
        break
    l = cv2.getTrackbarPos('L', 'image')
    u = cv2.getTrackbarPos('U', 'image')

    canny = cv2.Canny(img, l, u)

cv2.destroyAllWindows()