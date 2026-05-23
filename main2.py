import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np

model = YOLO('best.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  
        point = [x, y]
        print(point)


image = cv2.imread('test6.jpg')

my_file = open("coco1.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)

results = model.predict(image)
a = results[0].boxes.data
px = pd.DataFrame(a).astype("float")
#    print(px)

for index, row in px.iterrows():
#        print(row)
    x1 = int(row[0])
    y1 = int(row[1])
    x2 = int(row[2])
    y2 = int(row[3])
    d = int(row[5])
    c = class_list[d]

    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 255), 2)
    cvzone.putTextRect(image, f'{c}', (x1, y1), 1, 1)

cv2.imshow("RGB", image)
cv2.setMouseCallback('RGB', RGB)

cv2.waitKey(0)
cv2.destroyAllWindows()
