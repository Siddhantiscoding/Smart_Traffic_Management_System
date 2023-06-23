
from RGBTOGRAY import capturing
#from main import junction2 , junction3 , junction4
import cv2
import numpy as np

def overall():
    capturing()
    img = cv2.imread('/home/ysapi/Desktop/ProjectPython/Frame_1.jpg', 0)
    #  Find width and height of image
    row, column = img.shape

    #  Create an zeros array to store the sliced image
    img1 = np.zeros((row, column), dtype='uint8')
    #  Specify the min and max range
    min_range = 60

    max_range = 175
    #  Loop over the input image and if pixel value lies in desired range set it to 255 otherwise set it to 0.
    for i in range(row):
        for j in range(column):

            if img[i, j] > min_range and img[i, j] < max_range:
                img1[i, j] = 255

            else:
                img1[i, j] = 0  # img[i,j]     # a) 0 for without background and b) img[i,j] for wiothbackground

    #  Display the image
    cv2.imshow('Original image', img)
    cv2.imshow('sliced_with_bg', img1)
    cv2.imwrite('sliced_with_bg.tif', img1)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    J1_white = np.sum(img == 255)
    print("Junction (live) 1: " ,J1_white)
    return J1_white


overall()

    #junction2()
    #junction3()
    #junction4()