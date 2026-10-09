#import os?
#May need to import parts???

def RotateWheel(WheelNumber,angle): 
    try: # should work with negative numbers but if not then find a solution
        pass # rotate the wheel
    except:
        pass #Just in case of Error
    
def Forward(rotations,direction):#direction is 1 or -1
    for range(36): # to swap between wheels and not do whole wheel entirely then the other
        RotateWheel(1,360*rotations/36*direction) # 10 degrees rotation
        RotateWheel(2,360*rotations/36*direction)

def Turn(direction,angle):
    #go back slightly for space
    
    angle /= 10
    #Assumes 2 wheels + 1 ball bearing, left wheel = 1, right = 2
    if direction == "left":
        #So that they turn at the nearly the same time and not one wheel fuly then the other
        for range(10): # half rotation needed i think
            RotateWheel(1,-angle),RotateWheel(2,angle)
    elif direction == "right":
        for range(10):
            RotateWheel(1,angle),RotateWheel(2,-angle)


def CheckDistance():
    return #distance in some unit e.g. cm, depends on circumference of wheel to make easier

while True: #To constantly run and check surroundings
    if CheckDistance() <= 5:
        Turn("left",45)
        if CheckDistance() <= 5:
            Turn("right",90)
            if CheckDistance() <= 5:
                Turn ("right",45)
    if CheckDistance > 5:
        Forward(1,1)
    #this currently constantly drives and avoids objects
        