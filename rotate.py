x=int(input('X='))
y=int(input('Y='))
z=int(input('Z='))
x,y=y,x
y,z=z,y
print('After Rotation:')
print('X=',x)
print('Y=',y)
print('Z=',z)