import os

from ultralytics import YOLO
import cv2
import time

model = YOLO("yolov8s.pt")
cam_url = 'image.jpg'
annotate_path = "./annotate/tp"
i=1
flag = False
classes=[]

def coco(bbox, cls, frame):
    img_size = frame.shape[:2][::-1]
    # img_size = [1024, 768]

    # Compute normalized coordinates
    x, y, w, h = bbox
    normalized_x = x / img_size[0]
    normalized_y = y / img_size[1]
    normalized_w = w / img_size[0]
    normalized_h = h / img_size[1]

    # Combine into COCO format string
    coco_format = f"{cls} {normalized_x:.6f} {normalized_y:.6f} {normalized_w:.6f} {normalized_h:.6f}"

    print("coco- ",coco_format)  # Output: "1 0.585156 0.200391 0.425547 0.393229"
    return coco_format


while True:
    flag = False
    t1 = time.time()
    video = cv2.VideoCapture(cam_url)
    # video = cv2.VideoCapture(0)
    ret, frame = video.read()
    if ret:
        x = model.predict(source=frame)
        # print(x)
        coco_list=[]
        for box in x[0].boxes:
            cv2.imwrite(annotate_path + str(i) + ".jpg", frame)
            print("box-",box.numpy())
            bbox =  box.numpy()
            xywh = bbox.xywh[0]
            cls = round(bbox.cls[0])
            print("xywh-",xywh)
            coco_format =coco(xywh, cls, frame)

            # Get image filename without extension
            coco_list.append(coco_format)
            if coco_list!=[]:
                flag=True
        if flag:
            filename, ext = os.path.splitext("tp" + str(i) + ".jpg")

            with open(annotate_path + str(i) + ".txt", "w") as f:
                # Write contents of text list to file line by line
                for line in coco_list:
                    f.write(line + "\n")
            i = i + 1

