import cv2
from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")

import torch
USE_CUDA = torch.cuda.is_available()
device = torch.device('cuda:0' if USE_CUDA else 'cpu')
print(torch.cuda.is_available())
print(device)

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    result = model(frame, save = False)
    result = result[0].plot()
    cv2.imshow(' Camera', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break