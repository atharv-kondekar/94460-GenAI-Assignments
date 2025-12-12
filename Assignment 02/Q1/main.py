from area_calculations import *

print("-------- Welcome to Area Calculation Module -------- ")

shapes=["circle" , "rectangle" ,"triangle" ,"square"]

while True:
    print(" ->>>> Choose shape form the Following List ")
    
    i=1
    for s in shapes:
        print("",i,".",s)
        i=i+1

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            rad = float(input("Enter the Radius of the Circle : "))
            areaCircle(rad)
            

        case 2:
            len=float(input("Enter the lenght of the Rectangle : "))
            width=float(input("Enter the width of the Rectangle : "))
            areaRectangle(len,width)
            

        case 3:
            height=float(input("Enter the height of the triangle  : "))
            base=float(input("Enter the width of the Triangle: "))
            areaTriangle(base,height)
            

        case 4:
            side=float(input("Enter the side of the square  : "))
            areaSquare(side)
        

        case _ :
            print("invalid choice ")
            
        
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break

print(" ========== Thank you :) =========")