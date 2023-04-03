# link https://www.hackster.io/onedeadmatch/esp32-cam-python-stream-opencv-example-1cc205
import cv2 as cv
import numpy as np
import requests
import time



url="http://192.168.1.2"
def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")

set_resolution(url,9)
cap = cv.VideoCapture(url+":81/stream")




# while True:
#     if cap.isOpened():
#         ret, frame = cap.read()
#         frame = cv.resize(frame,(800,600), interpolation= cv.INTER_LINEAR)
#         cv.imshow("frame", frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         cv.destroyAllWindows()
#         break
            


def get_frame():
    if cap.isOpened():
        ret, frame = cap.read()
        frame = cv.resize(frame,(800,600), interpolation= cv.INTER_LINEAR)
    else:
        frame=None
    
    return frame


