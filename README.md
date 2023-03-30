# V8-AutoAnnotate
uses yolo v8 to do object detection and creates annotation in coco format.



This is a Python script that uses the YOLOv5 object detection model to detect objects in a video stream or a live camera feed. The script uses the "ultralytics" library to load the YOLOv5 model and the "cv2" library to capture frames from a camera or video stream. The script saves each frame with annotated object bounding boxes and their class labels.

The code initializes the YOLOv5 model with the "yolov8s.pt" weights file using the "YOLO" class from the "ultralytics" library. It sets the camera URL to capture the video stream or the live camera feed. The annotated frames are saved to the "annotate" folder with a file name that includes a counter value "i" that is incremented after each frame.

The code uses a while loop to continuously capture frames from the video stream. For each frame, the YOLOv5 model predicts the object bounding boxes and their class labels using the "predict" method. The code then saves the annotated frame to a file and writes the detected object bounding boxes and their class labels to a corresponding text file using the COCO (Common Objects in Context) format. The COCO format includes the class label and the normalized bounding box coordinates (x, y, w, h) of the detected object.

The script defines a "coco" function that takes the normalized bounding box coordinates and the class label and returns the COCO format string. The function converts the coordinates from pixel values to normalized values between 0 and 1, based on the image size. The script also initializes an empty list "coco_list" to store the COCO format strings for all detected objects in the current frame.

Finally, the script increments the counter value "i" to update the file name for the next annotated frame, and the while loop continues to capture and annotate the next frame from the video stream.
