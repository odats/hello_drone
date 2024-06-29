from djitellopy import Tello
import cv2

me = Tello()
me.connect()
print(me.get_battery())

me.streamon()

while True:
    img = me.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)

    # Check for key press; wait 1 millisecond
    key = cv2.waitKey(1)
    
    # Exit the loop if 'q' is pressed
    if key == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
me.streamoff()