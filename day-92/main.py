import os,cv2
from PIL import Image
from PIL import ImageMath
import os
import pandas as pd
import numpy as np


files_image_path = './images'
image_data = os.listdir(files_image_path)
print(' No# of images in data:', len(image_data))

# Create an empty list to store the image arrays
image_list = []

# Specify the folder path
folder_path = files_image_path

# Get a list of all the image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

# Iterate through the image files

    # Open the image file
img = Image.open(os.path.join(folder_path, image_files[0]))
    #img.show()
    # Convert the image to an array
img_array = np.array(img, dtype=object)


# Create a dataframe from the list of image arrays
#print(first_image.shape())

#df = pd.DataFrame(data=first_image, dtype=object)
#df.head()


image2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(image2)

f2 = pd.DataFrame(img_array[0])

f2.head()