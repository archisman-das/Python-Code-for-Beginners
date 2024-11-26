x1 = int(input("Enter the x coordinate of the first point : "))
y1 = int(input("Enter the y coordinate of the first point : "))
x2 = int(input("Enter the x coordinate of the second point : "))
y2 = int(input("Enter the y coordinate of the second point : "))
distance = ((x1-x2)**2+(y1-y2)**2)**0.5
print("Distance = "+ "%.2f"%distance)