import cv2
import numpy as np
import matplotlib.pyplot as plt

figuras = 'figuras.png'


def circleDetec(img_path):
    
    coins_img_gray = cv2.imread(img_path, 0)
    coins_img = cv2.imread(img_path)
    
    coins_circle = cv2.HoughCircles(coins_img_gray, 
                                    cv2.HOUGH_GRADIENT, 
                                    3, 
                                    100, 
                                    param1=100, 
                                    param2=150, 
                                    minRadius=80, 
                                    maxRadius=600)
    
    circles = coins_circle.reshape(-1, 3)
    circles = np.uint16(np.around(circles))
    for i in circles:
        lista=[196, 1556, 1586]
        #print(i[0])
        if i[0]==lista[0] or i[0]==lista[1] or i[0]==lista[2]:
          cv2.circle(coins_img, (i[0], i[1]), i[2], (0, 0, 255), 5)   #    
          cv2.circle(coins_img, (i[0], i[1]), 2, (0, 255, 0), 10)     #    
        else:
          continue
    
    
    titles = ['Circulos']
    images = [coins_img]
    miArray = np.arange(1)
    for i in miArray:
      plt.subplot(1,1,i+1),plt.imshow(images[i],'gray')
      plt.title(titles[i])
      plt.xticks([]),plt.yticks([])
 
    plt.show()
    
circleDetec(figuras)
