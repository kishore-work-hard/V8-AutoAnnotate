import os

import pandas as pd
from ultralytics import YOLO
import cv2
import time

model = YOLO("yolov8l.pt")
image_folder = "D:/kishore/DATA/project/Thampanoor/bike/bike data tampa"
annotate_path = "./annotate/tampa_bike_120_"
i=1
flag = False
classes=["Bike"]

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


for image_file in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_file)
    frame = cv2.imread(image_path)
    img_c = 0
    if frame is not None:
        x = model.predict(source=frame)
        a = x[0].boxes.boxes
        px = pd.DataFrame(a).astype("float")
        od_car = []
        od_bike = []
        od_lp = []

        for index, row in px.iterrows():
            # print("row-",row)
            cls = int(row[5])
            # car
            if cls == 3:
                # print(x)
                coco_list = []
                for box in x[0].boxes:
                    if img_c ==0:
                        cv2.imwrite(annotate_path + str(i) + ".jpg", frame)
                        print("box-", box.numpy())


                    bbox = box.numpy()
                    xywh = bbox.xywh[0]
                    cls = round(bbox.cls[0])
                    print("xywh-", xywh)
                    coco_format = coco(xywh, cls, frame)

                    # Get image filename without extension
                    coco_list.append(coco_format)
                    if coco_list != []:
                        flag = True
                if flag:
                    filename, ext = os.path.splitext(image_file)
                    if img_c ==0:
                        with open(annotate_path + str(i) + ".txt", "w") as f:
                            # Write contents of text list to file line by line
                            for line in coco_list:
                                f.write(line + "\n")
                        i = i + 1
                img_c = img_c + 1


