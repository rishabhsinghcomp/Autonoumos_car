import cv2 as cv
import numpy as np




helmate = cv.imread('Practice\helmate.jpg')
helmate = cv.resize(helmate,(600,400), interpolation= cv.INTER_LINEAR)


roi = helmate[0:200,200:600]

logo = cv.imread('Practice\logo.jpg')
logo = cv.resize(logo,(400,200), interpolation= cv.INTER_LINEAR)
logo = logo[200::,200::]
logo = cv.resize(logo,(400,200), interpolation= cv.INTER_LINEAR)

cv.imshow("logo",logo)

# grayscaling logo
gry_logo = cv.cvtColor(logo,cv.COLOR_BGR2GRAY)
cv.imshow("gry_logo",gry_logo)

# thresholding
ret,thresholded_img = cv.threshold(gry_logo,166,255,cv.THRESH_BINARY)

# inverting so main part(the logo) is in black
inv_thresholded_img = cv.bitwise_not(thresholded_img)
# created roi by and threhold(where main part is in black )
roi = cv.bitwise_and(roi,roi,mask=inv_thresholded_img)

#adding color to inverteed mask so main part has color
color = cv.bitwise_and(logo,logo,mask=thresholded_img)






roi = cv.add(color,roi)
cv.imshow("roi",roi)


helmate[0:200,200:600] = roi
cv.imshow("helmate",helmate)
# cv.imshow("inv_thresholded_img",inv_thresholded_img)

# cv.imshow("thresholded_img",thresholded_img)





cv.waitKey(0)
cv.destroyAllWindows()