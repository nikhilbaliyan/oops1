class Student:
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno
    def display(self):
        print('Name: {}, RollNo: {},'. \
              format(self.name, self.rno), end=' ')
s1 = Student('Nikhil', 13)
s1.display()

