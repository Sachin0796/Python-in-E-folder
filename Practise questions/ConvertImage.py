import cv2
#pip install opencv-python

image = cv2.imread("E:\Study\Python\All_codes\Practise questions\-6165857829437681030_121_1.jpg")

grey_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(grey_image)
blur=cv2.GaussianBlur(invert,(21,21),10)
invertedblur=cv2.bitwise_not(blur)
sketch=cv2.divide(grey_image, invertedblur,scale=256.0)
cv2.imwrite("E:\Study\Python\All_codes\Practise questions\sketch.png",sketch)