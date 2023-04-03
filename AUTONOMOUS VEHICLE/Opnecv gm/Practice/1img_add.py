import cv2 as cv
import numpy as np
import time





helmate = cv.imread('practicing\helmate.jpg')
helmate = cv.resize(helmate,(600,400), interpolation= cv.INTER_LINEAR)

main = cv.imread('practicing\main.jpg')
main = cv.resize(main,(600,400), interpolation= cv.INTER_LINEAR)




# # IMAGE ADDITION
# # np image addition
# new_np= main+helmate
# # cv image addtion
# new_cv= cv.add(main,helmate)

# cv.imshow("main",main)
# cv.imshow("helmate",helmate)
# cv.imshow("addiing using np_ image modulo",new_np)
# cv.imshow("addiing using cv_ image satueration",new_cv)




# IMAGE BELNIG\

# dst = cv.addWeighted(main,0,helmate,1,0) 
# cv.imshow("slide",dst)
# t=0
# while t<= 1:
#     slide =  cv.addWeighted(main,t,helmate,1-t,0)  #whwnver t=0 and other is greater meaing it is dominat
#     t= t+0.1
#     print(1-t)
#     cv.imshow("slide",slide)
#     cv.waitKey(300)





cv.destroyAllWindows()


