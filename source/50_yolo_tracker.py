from djitellopy import Tello
import cv2
from ultralytics import YOLO

me = Tello()
me.connect()
print(me.get_battery())

me.streamon()

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

while True:
    frame = me.get_frame_read().frame
    results = model.track(frame, persist=True)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLOv8 Tracking", annotated_frame)

    # Check for key press; wait 1 millisecond
    key = cv2.waitKey(1)
    
    # Exit the loop if 'q' is pressed
    if key == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
me.streamoff()