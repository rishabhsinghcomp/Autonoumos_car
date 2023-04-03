from esp_get import get_frame
import cv2 as cv
import numpy as np
from numpy import vstack,ones   
from numpy.linalg import lstsq
from statistics import mean


def process_img(org_img):
    proc_img= cv.cvtColor(org_img,cv.COLOR_BGR2GRAY)
    proc_img = cv.GaussianBlur(proc_img,(9,9),0)

    proc_img=cv.Canny(proc_img,threshold1=50,threshold2=100) # t1=200, t2=300
    return proc_img

def get_roi(img,vertices = np.array([[0,600],[0,300],[200,200],[600,200],[800,300],[800,600]])):
    mask= np.zeros_like(img)
    cv.fillPoly(mask,np.int32([vertices]),255)
    masked = cv.bitwise_and(mask,img)
    return masked


# enchancing line intensity  #DIDNT USE IT AS NOT REUQIRED
# def enhcancing_line(img):
#     kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
#     dilate = cv.dilate(img, kernel, iterations=1)
#     return dilate





# SENTDEX LANE DETECTOR
def draw_lanes(img, lines, color=[0, 255, 255], thickness=3):

    # if this fails, go with some default line
    try:

        # finds the maximum y value for a lane marker 
        # (since we cannot assume the horizon will always be at the same point.)

        ys = []  
        for i in lines:
            for ii in i:
                ys += [ii[1],ii[3]]
        min_y = min(ys)
        max_y = 600
        new_lines = []
        line_dict = {}

        for idx,i in enumerate(lines):
            for xyxy in i:
                # These four lines:
                # modified from http://stackoverflow.com/questions/21565994/method-to-return-the-equation-of-a-straight-line-given-two-points
                # Used to calculate the definition of a line, given two sets of coords.
                x_coords = (xyxy[0],xyxy[2])
                y_coords = (xyxy[1],xyxy[3])
                A = vstack([x_coords,ones(len(x_coords))]).T
                m, b = lstsq(A, y_coords)[0]

                # Calculating our new, and improved, xs
                x1 = (min_y-b) / m
                x2 = (max_y-b) / m

                line_dict[idx] = [m,b,[int(x1), min_y, int(x2), max_y]]
                new_lines.append([int(x1), min_y, int(x2), max_y])

        final_lanes = {}

        for idx in line_dict:
            final_lanes_copy = final_lanes.copy()
            m = line_dict[idx][0]
            b = line_dict[idx][1]
            line = line_dict[idx][2]
            
            if len(final_lanes) == 0:
                final_lanes[m] = [ [m,b,line] ]
                
            else:
                found_copy = False

                for other_ms in final_lanes_copy:

                    if not found_copy:
                        if abs(other_ms*1.2) > abs(m) > abs(other_ms*0.8):
                            if abs(final_lanes_copy[other_ms][0][1]*1.2) > abs(b) > abs(final_lanes_copy[other_ms][0][1]*0.8):
                                final_lanes[other_ms].append([m,b,line])
                                found_copy = True
                                break
                        else:
                            final_lanes[m] = [ [m,b,line] ]

        line_counter = {}

        for lanes in final_lanes:
            line_counter[lanes] = len(final_lanes[lanes])

        top_lanes = sorted(line_counter.items(), key=lambda item: item[1])[::-1][:2]

        lane1_id = top_lanes[0][0]
        lane2_id = top_lanes[1][0]

        def average_lane(lane_data):
            x1s = []
            y1s = []
            x2s = []
            y2s = []
            for data in lane_data:
                x1s.append(data[2][0])
                y1s.append(data[2][1])
                x2s.append(data[2][2])
                y2s.append(data[2][3])
            return int(mean(x1s)), int(mean(y1s)), int(mean(x2s)), int(mean(y2s)) 

        l1_x1, l1_y1, l1_x2, l1_y2 = average_lane(final_lanes[lane1_id])
        l2_x1, l2_y1, l2_x2, l2_y2 = average_lane(final_lanes[lane2_id])

        return [l1_x1, l1_y1, l1_x2, l1_y2], [l2_x1, l2_y1, l2_x2, l2_y2]
    except Exception as e:
        print(str(e))



# # drawing line on image
def draw_lines(img,lines):
    try:
       
        # for line in lines:
        #     cords = line[0]
        #     cv.line(img, (cords[0],cords[1]), (cords[2],cords[3]), [255,255,255], 7)


        lane1,lane2= draw_lanes(img,lines)
        cv.line(img, (lane1[0],lane1[1]), (lane1[2],lane1[3]), [255,255,255], 7)
        cv.line(img, (lane2[0],lane2[1]), (lane2[2],lane2[3]), [255,255,255], 7)
    except:
        pass


def get_lined_img(org_img,proc_img):
    # proc_img = enhcancing_line(proc_img)
    # return proc_img
    proc_img = cv.GaussianBlur(proc_img,(9,9),0)  #orginal blur was 3,3
    lines = cv.HoughLinesP(proc_img,1,np.pi/180, 180,np.array([]), minLineLength=15,maxLineGap=6)
    draw_lines(org_img,lines)
    return org_img








while 1:
    org_img= get_frame()
    proc_img=process_img(org_img) # gray > blur > canny
    vertices = np.array([[0,600],[0,300],[200,200],[600,200],[800,300],[800,600]])
    roi_img=get_roi(proc_img,vertices) #rhombus

    lined_img = get_lined_img(org_img,roi_img) #blur > houhlinesp > drawing
    cv.imshow("frame", lined_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break



