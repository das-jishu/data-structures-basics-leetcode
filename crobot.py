
class CRobot(object):
    def __init__(self):
        self.typeRobot = ""
        self.SN = 0
        self.orientation = 1
        self.status = False

    def __init__(self, typeRobot, sn):
        self.typeRobot = typeRobot
        self.SN = sn
        self.orientation = 1
        self.status = False

    def getType(self):
        return self.typeRobot

    def getSN(self):
        return self.SN

    def getOrientation(self):
        return self.orientation

    def getState(self):
        return self.status

    def setOrientation(self, x):
        self.orientation = x

    def setState(self, x):
        self.status = x

    def turn(self):
        if self.orientation == 1:
            self.orientation = 4
        else:
            self.orientation -= 1

    def display(self):
        print("Serial number :",self.SN)
        print("State :",self.status)
        print("Orientation :",self.orientation)
        print("Type :",self.typeRobot)


list_robot = []
for i in range(1,5):
    robot = CRobot("X-Man Robot", i)
    list_robot.append(robot)

for i in range(0, 4):
    list_robot[i].display()
    list_robot[i].setState(True)
    list_robot[i].setOrientation(i+1)
print("\n---\nUpdate of parameters\n---\n")
for i in range(0,4):
    list_robot[i].display()

    