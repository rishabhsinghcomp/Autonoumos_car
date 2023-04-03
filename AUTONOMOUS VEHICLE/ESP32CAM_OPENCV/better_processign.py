from esp_get import get_frame
import cv2 as cv
import sys
import numpy as np
# utility from nachiket273(Github) link>> https://github.com/nachiket273/Self_Driving_Car/blob/master/CarND-LaneLines-P1/helper.py
import helper_func as util
from helper_func import isolate_color_mask
import processing

# adding my function to dispaly multiple img on smae windows
sys.path.append(r"C:\Users\risha\OneDrive\Desktop\AUTONOMOUS VEHICLE\Opnecv gm\Practice")
from img_disp import mult_disp




# def color_selection(img,dark_img):
#     darkened_imgs=[img]
#     img_list=[img]
#     white_masks = [isolate_color_mask(img, np.array([210, 210, 210], dtype=np.uint8), np.array([255, 255, 255], dtype=np.uint8)) for img in img_list]
#     yellow_masks = [isolate_color_mask(img, np.array([190, 190, 0], dtype=np.uint8), np.array([255, 255, 255], dtype=np.uint8)) for img in img_list]
#     masked_imgs = []
#     for i in range(len(img_list)):
#         mask = cv.bitwise_or(white_masks[i], yellow_masks[i])
#         masked_imgs.append(cv.bitwise_and(darkened_imgs[i], darkened_imgs[i], mask=mask))

#     # display_imgs(masked_imgs, test_imgs)
#     return masked_imgs[0]






def contrast_stretch(gray):
    hist, bins = np.histogram(gray.ravel(), 256, [0, 256])
    min_intensity = np.where(hist > 0)[0][0]
    max_intensity = np.where(hist > 0)[0][-1]
    lut = np.zeros(256, dtype=np.uint8)
    lut[min_intensity:max_intensity+1] = np.linspace(0, 255, max_intensity-min_intensity+1)
    result = cv.LUT(gray, lut)
    return result


while 1:
    org_img= get_frame()
    gray = util.grayscale(org_img)
    blured= util.gaussian_blur(gray,21)

    # dark_gray= util.adjust_gamma(gray,0.5)
    

    # ret,thresholded_img = cv.threshold(gray,100,150,cv.THRESH_BINARY)


    # col_sel = color_selection(org_img,dark_gray)
    # mult_disp(dark_gray,canny,vid=True)

    contrasted= contrast_stretch(gray)
    canny = util.canny(gray,50,100)
    roi=processing.get_roi(canny)
    proc_img = cv.GaussianBlur(roi,(9,9),0)  #orginal blur was 3,3
    
    # lined = processing.get_lined_img(org_img,roi)


    # using helperfunc to get lines
    
    lines = cv.HoughLinesP(proc_img,1,np.pi/180, 180,np.array([]), minLineLength=15,maxLineGap=6)
    lane_lines=util.get_lane_lines(roi,lines)
    weighted_img =util.draw_weighted_lines(org_img,lane_lines)


    cv.imshow("window",weighted_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break

