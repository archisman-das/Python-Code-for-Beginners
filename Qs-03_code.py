# Name:Archisman Das Dept- Information Technology Sem - 3rd University Roll - 10900220058
# Write python program to calculate the area and perimeter of a circle, a square and a
# rectangle. Consider all the required information are preexisting.

# Perimeter & area of circle
import math
radius = float(input('Enter the radius of the circle: '))
per = 2*math.pi*radius
print('Perimeter of the circle: ',per,'unit')
area = math.pi * radius * radius
print('Area of the circle: ',area,'sq. units')

# Perimeter & area of square
side = float(input('Enter the side of the square: '))
print('Perimeter of the square: ',4*side, 'unit')
print('Area of the square: ',side*side,'sq. units')

# Perimeter & area of rectangle
length = float(input('Enter the length of the rectangle: '))
breadth = float(input('Enter the breadth of the rectangle: '))
peri = 2*(length+breadth)
print('Perimeter of the square: ',peri, 'unit')
print('Area of the square: ',length*breadth,'sq. units')