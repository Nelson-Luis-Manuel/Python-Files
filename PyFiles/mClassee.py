class MobileRobot:
    def __init__(self, position,width,length,height):
        self.position = position
        self.width = width
        self.length = length
        self.height = height
        self.status = 'iddle'
    
    def moveForward(self):
        self.status = 'Robot is moving forward!'
    
    def movebackWard(self):
        self.status = 'Robot is moving backward!'
    
    def moveRight(self):
        self.status = 'Robot is moving Right!'
    
    def moveLeft(self):
        self.status = 'Robot is moving left!'

    def stopMoving(self):
        self.status = 'Robot stopped!'

newRobot = MobileRobot(1,2,3,4)

newRobot.stopMoving()
print(newRobot.status)
newRobot.movebackWard()
print(newRobot.status)
newRobot.moveForward()
print(newRobot.status)
newRobot.moveLeft()
print(newRobot.status)
newRobot.moveRight()
print(newRobot.status)