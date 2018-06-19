class Temprature():
    def Fahrenhiet(self, celsius):
        x=(celsius * (9 / 5)) + 32
        print(x)

    def Celsius(self, farenhiet):
         y=(farenhiet - 32) * (5 / 9)
         print(y)
t = Temprature()
t.Fahrenhiet(25)
t.Celsius(275)
