a = float(input("Enter the first side of triangle:"))
b = float(input("Enter the second side of triangle:"))
c = float(input("Enter the third side of triangle:"))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area =" + str(round(area,2)))