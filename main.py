import door
#import led #uncomment when ready and installed all required packages
import camera


def main():
    # where all the main stuff goes
    # make all display features in main

    # example of creating and calling a constructor
    door1 = door.Door(name='door1', buttonpin=3)
    print(door1.name)
    #

    #Checking if main was called
    print(0)
    return 0


if __name__ == "__main__":
    main()
