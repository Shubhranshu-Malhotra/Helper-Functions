################# IMPORTS ###################
import cv2
import matplotlib.pyplot as plt
import numpy as np
#############################################


### Display Images ###

def imshow(image = None, title = "", size = 10, bgr_2_rgb = True, grayscale = False):
    """
    Display image using matplotlib pyplot
    title: Title for the image
    img_path: Loaded image
    bgr_2_rgb: Convert image from BGR to RGB scale
    grayscale: Convert image to gray scale
    """
    if grayscale == True:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if bgr_2_rgb == True:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    h, w, c = np.array(image).shape
    aspect_ratio = h/w
    plt.figure(figsize=(size*aspect_ratio, size))
    plt.imshow(img)
    plt.title(title)
    plt.show()


