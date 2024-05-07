from ultralytics import YOLO
import os
import cv2
import numpy

def gen_label(size=(640, 640)):
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    fontScale              = .8
    fontColor              = (0, 255, 0)
    thickness              = 2
    lineType               = 2
    model = YOLO("yolov8n-pose.pt")
    path = "images/"
    images = [cv2.imread(path + val) for val in os.listdir(path)]
    images = [cv2.resize(img, size) for img in images]
    images = numpy.array(images)
    j=0
    for img in images:
        result = model(img, save=False)
        result = result[0]
        bboxes = result.boxes.xyxy
        keypoints = result.keypoints.data.cpu().detach().numpy().astype(str)
        pltimg = result.plot()
        print(len(keypoints))
        for i in range(len(bboxes)):
            bbox = bboxes[i]
            pltimg = cv2.putText(pltimg,f"person: {i}", 
                                (int(bbox[0]), int(bbox[3])), 
                                font, 
                                fontScale,
                                fontColor,
                                thickness,
                                lineType)
        cv2.imwrite(f'pltimages/img_{j}.jpg', pltimg)
        save_str = [val.flatten() for val in keypoints]
        save_str = [' '.join(val) for val in save_str]
        save_str = '\n'.join(save_str)
        with open(f"labels/img_{j}.txt", 'w') as file:
            file.write(save_str)
        j+=1
        
if __name__ == "__main__":
    gen_label()