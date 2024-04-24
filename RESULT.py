
!pip install ultralytics==8.0.196

from ultralytics import YOLO
import cv2

from IPython.display import display, Image



!yolo task=detect mode=predict model=/content/best.pt conf=0.5 source=/content/IMG_20221119_174658.jpg save=True

Image(filename="/content/runs/detect/predict/IMG_20221119_174658.jpg", width=200)
#set width =600

!yolo task=detect mode=predict model=/content/best.pt conf=0.3 source=/content/sixteen-miles-out-oDfeFV-Y2v0-unsplash.jpg save=True

Image(filename="/content/runs/detect/predict4/sixteen-miles-out-oDfeFV-Y2v0-unsplash.jpg", width=200)
#set width =600
