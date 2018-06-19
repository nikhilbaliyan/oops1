class circle():
    def __init__(self, r):
        self.radius = r
    def getarea(self):
        y=3.14*self.radius *self.radius
        print(y)
    def circumfrance(self):
        x= 2 *  3.14 *self.radius
        print(x)
new = circle(8)
new.getarea()
new.circumfrance()