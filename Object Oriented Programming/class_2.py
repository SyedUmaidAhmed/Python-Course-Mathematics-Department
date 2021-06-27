class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name

    def work(self):
        print("Hello the work is goin on: ", self.name)

square = Polygon(4, "Square")
square.work()



