# Used to convert images to a numpy array

# Import the necessary libraries
import cv2 as cv
import numpy as np

# load the image and convert into numpy array of avg
# of r g b values
def numpyImg(imgName):
    # load image
    img = cv.imread(imgName)

    #create the numpy array based on the image
    data = np.array([img])

    # get the height, width, dim
    height, width, dim = img.shape

    # create the averages array
    avgs = [[0] * dim for _ in range(height)]

    # initialize R G B avg values
    totalR = 0 
    totalG = 0
    totalB = 0

    # return b g r value of each pixel in the image
    for i in range(height):
        for j in range(width):
            pxlB, pxlG, pxlR = img[i, j]

            # add the total of each color value for the row
            totalR += pxlR
            totalG += pxlG
            totalB += pxlB

        # calculate the average of R G B of the row
        rAvg = totalR / width
        gAvg = totalG / width
        bAvg = totalB / width

        # place averages in an array
        for k in range(dim):
            if(k == 0):
                avgs[i][k] = int(rAvg)
            elif(k == 1):
                avgs[i][k] = int(gAvg)
            elif(k == 2):
                avgs[i][k] = int(bAvg)
        
        # reset totals for calculating averages of next row
        totalR = 0
        totalG = 0
        totalB = 0
    
    # print the avgs array
    print(avgs)
