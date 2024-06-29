import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((100, 100))


def getKey(keyName):
    ans = False

    # Pygame maintains an event queue that collects events such as key presses, mouse movements, and window interactions (like closing the window). 
    # If you do not process these events, they will accumulate and may cause your program to become unresponsive. 
    # The line for eve in pygame.event.get(): pass ensures that the event queue is emptied, preventing this issue.
    for eve in pygame.event.get(): pass

    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, f'K_{keyName}')
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    
    return ans


def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key Pressed")


if __name__ == '__main__':
    init()
    while True:
        main()