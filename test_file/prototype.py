import numpy as np
import math
import cv2

global WIDTH, HEIGHT, FR
WIDTH = 800
HEIGHT = 450
FR = 60

class Frame:
    def __init__(self):
        self.frame = np.zeros([HEIGHT, WIDTH, 3])
    
    def coordinate_system(self, x_min, x_max, y_min, y_max):
        self.x = np.arange(x_min, x_max, (x_max-x_min)/WIDTH)
        self.y = np.arange(y_min, y_max, (y_max-y_min)/HEIGHT)
        self.coordinate = np.flipud([[[i,j] for j in self.x] for i in self.y])

def function(x,y):
    return x**2 
  
image = Frame()
image.coordinate_system(0,4,0,2)
epsilon = 0.01
for j,x in enumerate(image.coordinate):
    for i,y in enumerate(x):
        f = function(x,y)
        if abs(f - y) <= epsilon:
            image.frame = cv2.circle(image.frame, (j,i), 2, (255,255,255), -1)
cv2.imshow("Prototype", np.uint8(image.frame))
cv2.waitKey(0)
    
