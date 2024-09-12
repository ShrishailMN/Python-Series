while True:
    print("1.Area of Square\n","2.Area of Rectangle\n","3.Area of Triangle\n","4.Area of Circle")
    num=int(input("Enter the option: "))
    if num==1:
        side=int(input("Enter the side of Square "))
        print("Area of Square is ",side*side)
    elif num==2:
        length=int(input("Enter the length of rectangle: "))
        bredth=int(input("Enter the bredth of the rectangle: "))
        print("Area of rectangle is ",length*bredth)
    elif num==3:
        base=int(input("Enter the base of triangle: "))
        height=int(input("Enter the height of triangle: "))
        print("Area of triangle is",0.5*base*height)
    elif num==4:
        radius=int(input("Enter the radius of the circle"))
        print("Area of circle is ",3.14*radius*radius)
    elif num==5:
        exit(0)
        break
    else:
        print("Invalid Input")