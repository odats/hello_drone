from ultralytics import YOLO


# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolov8n.pt")

results = model.track(source=1, show=True, tracker="bytetrack.yaml")


# Perform object detection on an image using the model
# results = model("https://ultralytics.com/images/bus.jpg")
# print(results)
