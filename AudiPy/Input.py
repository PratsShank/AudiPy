# Import the necessary libraries
import cv2 
import numpy as np
import os

class Input:

    def __init__(self):
        return

    def take_file(self, filename):
        
        file_ext = os.path.splitext(filename)[1].lower()

        print('yuh')

        if file_ext in [".csv"]:
            array = self.read_dataset_csv(filename)
            #array = wrapcsv(array)
            return array
        elif file_ext in [".jpg", ".png"]:
            array = self.read_dataset_img(filename)
            #array = wrapimg(array)
            return array
        else:
            raise ValueError("Error, file type not matching")
        

    # Input for CSV files that will convert to numpy files for processing
    def read_dataset_csv(self, filename):
        """Reads a CSV file into a numpy DataFrame."""
        data = np.loadtxt(filename, delimiter= ",")
        # Return the data set of numpy
        return data

    # load the image and convert into numpy array of avg
    # of r g b values
    def read_dataset_img(self, imgName):
        # Used to convert images to a numpy array


        # load image
        #img = cv.imread(imgName)

        #print(img)
        
        ###STOP###

        # Load the image (ensure it's in color)
        image = cv2.imread(imgName)  # Replace with your image path

        # Convert from BGR (OpenCV default) to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Get image dimensions (height, width, channels)
        _, width, _ = image.shape

        # Lists to store average R, G, and B values for each column
        avg_r_values = []
        avg_g_values = []
        avg_b_values = []

        #ADDED
        avg_rgb_values = []
        # Loop through each column
        for col in range(width):
            # Extract the column (all rows, specific column)
            column_pixels = image[:, col, :]  # Shape (height, 3)
            
            # Compute the mean for each color channel
            avg_r = np.mean(column_pixels[:, 0])  # Red channel
            avg_g = np.mean(column_pixels[:, 1])  # Green channel
            avg_b = np.mean(column_pixels[:, 2])  # Blue channel

            #ADDED
            #avg_rgb = np.mean(column_pixels[:,:],axis=0)
            #avg_rgb_values.append(avg_rgb)
            # Store values
            avg_r_values.append(avg_r)
            avg_g_values.append(avg_g)
            avg_b_values.append(avg_b)

        # Convert lists to NumPy arrays for efficient computation
        avg_r_values = np.array(avg_r_values)
        avg_g_values = np.array(avg_g_values)
        avg_b_values = np.array(avg_b_values)

        #ADDED
        avg_rgb_values = np.stack((avg_r_values, avg_g_values, avg_b_values), axis=0)
        #print(avg_rgb_values)

        return avg_rgb_values

        #print(avg_rgb_values)
        #np.savetxt("rgb_averages1.csv", avg_rgb_values, delimiter=" ", fmt="%.0f", header="", comments="")
        #np.savetxt("rgb_averages1.csv", avg_rgb_values, delimiter=",")