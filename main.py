from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator


Auto_Swerve = False

def Turn_Left(seconds):
    robot.motors(BACKWARD, FORWARD, seconds)

def Turn_Right(seconds):
    robot.motors(FORWARD, BACKWARD, seconds)

Left_Object_Distance = robot.left_sonar()
Right_Object_Distance = robot.right_sonar()

if Left_Object_Distance == 0:
    print("COOLLISSIONNN!")

if Right_Object_Distance == 0:
    print("COOLLISSIONNN!")

if Left_Object_Distance < 10:
    print("Object Approaching On The Left!")

if Right_Object_Distance < 10:
    print("Object Approaching On The Right!")

if Auto_Swerve == True:
    if Left_Object_Distance < 5:
        Turn_Right(5)

if Auto_Swerve == True:
    if Right_Object_Distance < 5:
        Turn_Left(5)

Turn_Left(90*(6.12/360))

robot.exit()