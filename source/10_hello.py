from djitellopy import Tello

tello = Tello()

tello.connect()

print(tello.get_battery())

# tello = Tello()

# tello.connect()

tello.takeoff()
tello.flip_left()
tello.land()

tello.send_rc_control(0, 0, 0, 0)

# tello.takeoff()

#tello.move_left(100)
# tello.rotate_counter_clockwise(90)
# tello.move_forward(100)

# tello.land()