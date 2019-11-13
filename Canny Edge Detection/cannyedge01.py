
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logos.jpg',0)
edges = cv2.Canny(img,100,110)

plt.subplot(2,1,1),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2),plt.imshow(edges,cmap = 'gray')
plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])

plt.show()

1
2
3
4
5
6
7
8
9
10
11
12
13
14
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('logos.jpg',0)
edges = cv2.Canny(img,100,110)
 
plt.subplot(2,1,1),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2),plt.imshow(edges,cmap = 'gray')
plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])
 
plt.show()