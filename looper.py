class Ball:
    def __init__(self,color,size,direction):
        self.color = color
        self.size = size
        self.direction = direction

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball("red","small","down")
print("I just created a ball")
print("My ball size is",myBall.size)
print("My ball color is",myBall.color)
myBall.bounce()
print("Now my ball's direction is",myBall.direction)
