import cv2 as cv
import numpy as np


# function to display multiple images in one windows
def mult_disp(*args,width=500,height=500,vid=False):
    k=[]
    for i in args:
        i= cv.resize(i,(width,height), None,0.5,0.5)
        if len(i.shape)<3:
            i = cv.cvtColor(i,cv.COLOR_GRAY2BGR)
        k.append(i)
    
    s = len(k)
    hstacks=[]
    ind=0
    while(s>3):
        h = np.hstack(tuple(k[ind:ind+3]))
        s=s-3
        ind=ind+3
        hstacks.append(h)
    


    # checking any left elements
    if(s!=0):

        # h=np.hstack(tuple(k[ind::]))
        # hstacks.append(h)
        temp=k[ind::]

        # making sure htack is not incompatible
        if(s!=3):
            for i in range(3-s):
                blank_image = np.zeros((height, width, 3), np.uint8)
                temp.append(blank_image)
        h=np.hstack(tuple(temp))
        hstacks.append(h)

    final = np.vstack(tuple(hstacks))
    if vid==False:
    
        cv.imshow("images",final)
        # hstack = np.hstack(tuple(k))
        # cv.imshow("hstack",hstack)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        cv.imshow("images",final)
