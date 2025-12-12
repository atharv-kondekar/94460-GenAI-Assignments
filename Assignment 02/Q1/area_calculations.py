import math
def areaCircle(radius):
    print("Area of the Circle : ",math.pi*radius*radius)

def areaRectangle(lenght,width):
    print("Area of the Rectangle : ",lenght*width)

def areaSquare(side):
    print("Area of the Square : ",side*side)

def areaTriangle(base,height):
    print("Area of the triangle : ",0.5*base*height)

if __name__=="__main__":
    areaCircle(2.4)
    areaRectangle(1,3)
    areaSquare(4)
    areaTriangle(1.1,3.4)
