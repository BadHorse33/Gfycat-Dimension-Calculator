import math

class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getNearestDivisibleWidth(self):
        for i in range(self.x, 2, -2):
            j = int((i/self.x)*self.y)
            if i % 16 == 0 and j % 16 == 0:
                return (i,j)
        print("couldn't find a good dimension")
        return [0,0]

'''
if __name__ == '__main__':
    x,y = input("please enter dimensions: ").split("x")
    r = Rectangle(int(x), int(y))
    tuple = r.getNearestDivisibleWidth()
    print(tuple)
'''