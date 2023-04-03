import cv2 as cv
import numpy as np



# Load two images
# img1 = cv.imread('test purpose\main.jpg')
# img1 = cv.resize(img1,(800,600), interpolation= cv.INTER_LINEAR)
# img2 = cv.imread('test purpose\logo.png')
# img2 =  cv.resize(img2,(400,200), interpolation= cv.INTER_LINEAR)

# assert img1 is not None, "file could not be read, check with os.path.exists()"
# assert img2 is not None, "file could not be read, check with os.path.exists()"

# # I want to put logo on top-left corner, So I create a ROI
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols]
# # Now create a mask of logo and create its inverse mask also
# img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
# ret, mask = cv.threshold(img2gray, 26, 255, cv.THRESH_BINARY)
# mask_inv = cv.bitwise_not(mask)

# cv.imshow('mask',mask)
# cv.imshow("mask inverted",mask_inv)
# cv.imshow("orgn",img2)
# cv.imshow("gryscaled",img2gray)

# cv.imshow("roi",roi)

# # # Now black-out the area of logo in ROI
# # img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# # cv.imshow("img1_bg",img1_bg)

# # # Take only region of logo from logo image.
# # img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# # cv.imshow("img2_bg",img2_fg)

# # # Put logo in ROI and modify the main image
# # dst = cv.add(img1_bg,img2_fg)
# # cv.imshow("dst",dst)
# # img1[0:rows, 0:cols ] = dst
# # cv.imshow('res',img1)
# cv.waitKey(0)
# cv.destroyAllWindows()







# PRACTICING
# imporitng images
helmate = cv.imread('test purpose\helmate.jpg')
helmate = cv.resize(helmate,(800,600), interpolation= cv.INTER_LINEAR)

main = cv.imread('test purpose\main.jpg')
main = cv.resize(main,(800,600), interpolation= cv.INTER_LINEAR)
logo = cv.imread('test purpose\logo.png')
logo =  cv.resize(logo,(400,200), interpolation= cv.INTER_LINEAR) #resize argument takes(width,height) or (column,row)
# cv.imshow('main',main)
# cv.imshow('logoq',logo)


# gryscaling images
gry_logo = cv.cvtColor(logo,cv.COLOR_BGR2GRAY)
# cv.imshow('graylogo',gry_logo)
# threholding and creating mask
ret, mask = cv.threshold(gry_logo, 30, 255, cv.THRESH_BINARY)#threhold below 330 is zero and aboce 30 is 1
# cv.imshow('mask',mask)
# creating inverted mask
mask_inv = cv.bitwise_not(mask)
# cv.imshow('inv_mask',mask_inv)



# creating section in which mask will be planted'
print(logo.shape[0])
roi = main[300:300+logo.shape[0],300:300+logo.shape[1]]
t1=helmate[400:400+200,0:400]
main_roi = cv.bitwise_and(roi,t1,mask=mask_inv) 	    #i still have doubts about this

cv.imshow('t1',roi)


cv.imshow('roi',main_roi)

color_logo_section=cv.bitwise_and(logo,logo,mask=mask)
# cv.imshow("coloured region",color_logo_section)

ored_img= cv.bitwise_or(color_logo_section,main_roi)
# cv.imshow("ored",ored_img)


main[300:300+logo.shape[0],300:300+logo.shape[1]]= ored_img
# cv.imshow("main",main)






cv.waitKey(0)
cv.destroyAllWindows()



