import cv2
import numpy as np
from matplotlib import pyplot as plt #used for displaying frames

#Basics: Load image in grayscale
img = cv2.imread('testimg/portrait.jpg',cv2.IMREAD_GRAYSCALE)


#Dispalying image result with matplotlib
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
#plt.show()


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#save new image
cv2.imwrite('watchgray.png',img)
