from djitellopy import Tello
import time

def main():
    tello = Tello()

    # Connect to the Tello drone
    tello.connect()

    # Check battery status
    battery = tello.get_battery()
    print(f"Battery life: {battery}%")

    print("Enter Python commands to control the drone (type 'quit' to exit):")

    # Dictionary to provide access to the Tello object in exec context
    context = {'tello': tello}

    while True:
        command = input(">>> ")
        if command == "quit":
            break
        try:
            # tello.takeoff()
            # tello.move_left(50)
            exec(command, context)
        except Exception as e:
            print(f"Error executing command '{command}': {e}")
        time.sleep(1)  # Small delay to ensure the command is processed

    # Ensure the drone lands if the script exits
    tello.land()

if __name__ == '__main__':
    main()