import cv2
img=cv2.imread('lena.png')
classNames=[]
classFile='coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('n').split('n')

cv2.imshow("Output",img)
# cv2.waitKey(10)