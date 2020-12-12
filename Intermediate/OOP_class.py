import random
width=100
height=200

class Blob:
    def __init__(self,color):

        self.x=random.randrange(0,width)
        self.y=random.randrange(0,height)
        self.size=random.randrange(4,8)
        self.color=color
    def move(self):

        self.move_x=random.randrange(-1,2)
        self.move_x = random.randrange(-1,2)
        self.x+=self.move_x
        self.y += self.move_y

        if self.x<0: self.x=0
        elif self.x>width: self.x = width
        if self.y<0: self.y=0
        elif self.y>height: self.y = height