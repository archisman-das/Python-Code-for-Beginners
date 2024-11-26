#Enter a digit N and further find out the sum of (N + NN + NNN),i.e., if N = 5, then sum = (5+55+555) = 615.
#Name:Archisman Das Stream:Information Technology University Roll No:10900220058
n = int(input("Enter a number:"))
s = 100*n + 20*n + 3*n
print("The Sum is: ",end="%d"%(s))