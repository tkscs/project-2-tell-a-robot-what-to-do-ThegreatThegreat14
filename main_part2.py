from simulator import robot, FORWARD, BACKWARD, STOP

# define trick and name and have it auto add to trick list
# check possible tricks

# number of seconds it takes to turn one degree
degree = 6.12/360 # 6.12 seconds = 360 degrees
# need to turn in 30 degree intervals to be at least 0.5 seconds

def Turn_Clock(seconds):
    '''
    turn right for 'seconds' amount of seconds
    '''
    robot.motors(BACKWARD, FORWARD, seconds)

def Turn_Counter_Clock(seconds):
    '''
    turn left for 'seconds' amount of seconds
    '''
    robot.motors(FORWARD, BACKWARD, seconds)

def Forward(seconds):
    '''
    go forward for 'seconds' amount of seconds
    '''
    robot.motors(FORWARD, FORWARD, seconds)

def Backward(seconds):
    '''
    go backward for 'seconds' amount of seconds
    '''
    robot.motors(BACKWARD, BACKWARD, seconds)

def Is_Int(Limit):
    '''
    check if 'limit' is an integer and returns True or False
    '''
    try:
        int(Limit)
        return True
    except ValueError:
        return False

def Spin_Left():
    '''
    spin left 360 degrees
    '''
    for i in range(12):
        Left_Object_Distance = robot.left_sonar()
        Right_Object_Distance = robot.right_sonar()
        if Left_Object_Distance > 5 and Right_Object_Distance > 5:
            Block = "No"
            Turn_Counter_Clock(30*degree)
        elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
            Block = "Yes"
    if Block == "Yes":
        print("Uh oh! There's something in my way.")

def Spin_Right():
    '''
    spin right 360 degrees
    '''
    for i in range(12):
        Left_Object_Distance = robot.left_sonar()
        Right_Object_Distance = robot.right_sonar()
        if Left_Object_Distance > 5 and Right_Object_Distance > 5:
            Block = "No"
            Turn_Clock(30*degree)
        elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
            Block = "Yes"
    if Block == "Yes":
        print("Uh oh! There's something in my way.")

def Square_Left():
    '''
    make a square moving left
    '''
    for i in range(4):
        for i in range(4):
            Left_Object_Distance = robot.left_sonar()
            Right_Object_Distance = robot.right_sonar()
            if Left_Object_Distance > 5 and Right_Object_Distance > 5:
                Block = "No"
                Forward(0.5)
            elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
                Block = "Yes"
        for i in range(3):
            Left_Object_Distance = robot.left_sonar()
            Right_Object_Distance = robot.right_sonar()
            if Left_Object_Distance > 5 and Right_Object_Distance > 5:
                Block = "No"
                Turn_Counter_Clock(30*degree)
            elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
                Block = "Yes"
    if Block == "Yes":
        print("Uh oh! There's something in my way.")

def Square_Right():
    '''
    make a square moving right
    '''
    for i in range(4):
        for i in range(4):
            Left_Object_Distance = robot.left_sonar()
            Right_Object_Distance = robot.right_sonar()
            if Left_Object_Distance > 5 and Right_Object_Distance > 5:
                Block = "No"
                Forward(0.5)
            elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
                Block = "Yes"
        for i in range(3):
            Left_Object_Distance = robot.left_sonar()
            Right_Object_Distance = robot.right_sonar()
            if Left_Object_Distance > 5 and Right_Object_Distance > 5:
                Block = "No"
                Turn_Clock(30*degree)
            elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
                Block = "Yes"
    if Block == "Yes":
        print("Uh oh! There's something in my way.")

def Turn_Left(Turn_Amount): ###
    '''
    turn left 'Turn_Amount' degrees
    '''
    for i in range(round(((Turn_Amount)*(6.12/180)))-1):
        Left_Object_Distance = robot.left_sonar() #centimeters
        Right_Object_Distance = robot.right_sonar() #centimeters
        if Left_Object_Distance > 5 and Right_Object_Distance > 5:
            Block = "No"
            Turn_Counter_Clock((180/6.12)*(degree)) # turn 0.5 seconds
        elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
            Block = "Yes"
    Left_Object_Distance = robot.left_sonar() #centimeters
    Right_Object_Distance = robot.right_sonar() #centimeters
    if Left_Object_Distance > 5 and Right_Object_Distance > 5:
        Block = "No"
        Turn_Counter_Clock((((Turn_Amount)*degree)-(round((Turn_Amount)*(6.12/180))))+((180/6.12)*(degree)))
    elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
        Block = "Yes"
    if Block == "Yes":
        print("Uh oh! There's something in my way.")

def Turn_Right(Turn_Amount):
    '''
    turn right 'Turn_Amount' degrees
    '''
    for i in range(round(((Turn_Amount)*(6.12/180)))-1):
        Left_Object_Distance = robot.left_sonar() #centimeters
        Right_Object_Distance = robot.right_sonar() #centimeters
        if Left_Object_Distance > 5 and Right_Object_Distance > 5:
            Block = "No"
            Turn_Clock((180/6.12)*(degree)) # turn 0.5 seconds
        elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
            Block = "Yes"
    Left_Object_Distance = robot.left_sonar() #centimeters
    Right_Object_Distance = robot.right_sonar() #centimeters
    if Left_Object_Distance > 5 and Right_Object_Distance > 5:
        Block = "No"
        Turn_Clock((((Turn_Amount)*degree)-(round((Turn_Amount)*(6.12/180))))+((180/6.12)*(degree)))
    elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
        Block = "Yes"
    if Block == "Yes":
        print("Uh oh! There's something in my way.")

def Forward_Trick(Forward_Amount):
    '''
    go forward 'Forward_Amount' seconds
    '''
    if int(Forward_Amount) < 0.5:
        Left_Object_Distance = robot.left_sonar()
        Right_Object_Distance = robot.right_sonar()
        if Left_Object_Distance > 5 and Right_Object_Distance > 5:
            Block = "No"
            Forward(Forward_Amount)
        elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
            Block = "Yes"
    else:
        for i in range(int((Forward_Amount)*2)):
            Left_Object_Distance = robot.left_sonar()
            Right_Object_Distance = robot.right_sonar()
            if Left_Object_Distance > 5 and Right_Object_Distance > 5:
                Block = "No"
                Forward(0.5)
            elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
                Block = "Yes"
        Left_Object_Distance = robot.left_sonar()
        Right_Object_Distance = robot.right_sonar()
        if Left_Object_Distance > 5 and Right_Object_Distance > 5:
            Block = "No"
            Forward(((Forward_Amount)*2)-(int((Forward_Amount)*2)))
        elif Left_Object_Distance <= 5 or Right_Object_Distance <= 5:
            Block = "Yes"
        if Block == "Yes":
            print("Uh oh! There's something in my way.")

def Backward_Trick(Backward_Amount):
    '''
    go backward 'Backward_Amount' seconds
    '''
    Backward(Backward_Amount)

############################################################################################################

Request = input("Hello, I am a robot! I can do cool tricks! If you want to know what tricks I can do and how to request them, reply T, and if you want me to power down, reply D. ")
while True:
    if Request == "T":
        What_Trick = input("I can spin for S, do a square for Q, turn for N, go forward for F, go backward for B, turn right for R, and turn left for L. ")
        while True:
            if What_Trick == "S":
                Spin_Direction = input("Would you like to spin left for L or right for R? ")
                while True:
                    if Spin_Direction == "L":
                        Spin_Left()
                        What_Trick = input("What trick do you want me to do now? ")
                        break
                    elif Spin_Direction == "R":
                        Spin_Right()
                        What_Trick = input("What trick do you want me to do now? ")
                        break
                    elif Spin_Direction == "D":
                        What_Trick = "D"
                        Request = "D"
                        break
                    else:
                        Spin_Direction = input("Please respond with L or R. ")
            elif What_Trick == "Q":
                Square_Direction = input("Would you like to go left for L or right for R? ")
                while True:
                    if Square_Direction == "L":
                        Square_Left()
                        What_Trick = input("What trick do you want me to do now? ")
                        break
                    elif Square_Direction == "R":
                        Square_Right()
                        What_Trick = input("What trick do you want me to do now? ")
                        break
                    elif Square_Direction == "D":
                        What_Trick = "D"
                        Request = "D"
                        break
                    else:
                        Square_Direction = input("Please respond with L or R. ")
            elif What_Trick == "N":
                Turn_Direction = input("Would you like to turn left for L or right for R? ")
                while True:
                    if Turn_Direction == "L":
                        Turn_Amount = input("How many degrees would you like to turn? ")
                        while True:
                            if Is_Int(Turn_Amount) == True:
                                Turn_Left(int(Turn_Amount))
                                What_Trick = input("What trick do you want me to do now? ")
                                break
                            else:
                                Turn_Amount = input("Please respond with a number. ")
                        break
                    elif Turn_Direction == "R":
                        Turn_Amount = input("How many degrees would you like to turn? ")
                        while True:
                            if Is_Int(Turn_Amount) == True:
                                Turn_Right(int(Turn_Amount))
                                What_Trick = input("What trick do you want me to do now? ")
                                break
                            else:
                                Turn_Amount = input("Please respond with a number. ")
                        break
                    elif Turn_Direction == "D":
                        What_Trick = "D"
                        Request = "D"
                        break
                    else:
                        Turn_Direction = input("Please respond with L or R. ")
            elif What_Trick == "F":
                Forward_Amount = input("How far would you like to go? ")
                while True:
                    if Is_Int(Forward_Amount) == True:
                        Forward_Trick(int(Forward_Amount))
                        What_Trick = input("What trick do you want me to do now? ")
                        break
                    else:
                        Forward_Amount = input("Please respond with a number. ")
            elif What_Trick == "B":
                Backward_Amount = input("How far would you like to go? ")
                while True:
                    if Is_Int(Backward_Amount) == True:
                        Backward_Trick(int(Backward_Amount))
                        What_Trick = input("What trick do you want me to do now? ")
                        break
                    else:
                        Backward_Amount = input("Please respond with a number. ")
            elif What_Trick == "R":
                Turn_Right(90)
                What_Trick = input("What trick do you want me to do now? ")
            elif What_Trick == "L":
                Turn_Left(90)
                What_Trick = input("What trick do you want me to do now? ")
            elif What_Trick == "D":
                Request = "D"
                break
            else:
                What_Trick = input("Please respond with S, Q, N, F, B, R, or L. ")
    elif Request == "D":
        print("Okay, goodbye, I am powering down.")
        break
    else:
        Request = input("Please respond with T or D. ")

robot.exit()