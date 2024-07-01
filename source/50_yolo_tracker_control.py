from djitellopy import Tello
import cv2
from ultralytics import YOLO

from time import sleep
import time
import keypress_module as kp
kp.init()

me = Tello()
me.connect()
print(me.get_battery())

me.streamon()

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): 
        lr = -speed
    elif kp.getKey("RIGHT"): 
        lr = speed

    if kp.getKey("UP"): 
        fb = speed
    elif kp.getKey("DOWN"): 
        fb = -speed

    if kp.getKey("w"): 
        ud = speed
    elif kp.getKey("s"): 
        ud = -speed

    if kp.getKey("a"): 
        yv = speed
    elif kp.getKey("d"): 
        yv = -speed

    if kp.getKey("q"): 
        me.land()
        sleep(3)

    if kp.getKey("e"): 
        me.takeoff()

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

    frame = me.get_frame_read().frame
    results = model.track(frame, persist=True)

    # Visualize the results on the frameqq
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