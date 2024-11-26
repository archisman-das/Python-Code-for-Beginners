negatives = positives = zeroes = 0
print("Enter -1 to exit....")
while(1):
    num = int(input("Enter any number: "))
    if(num == -1):
        break
    if(num ==0):
        zeroes = zeroes+1
    elif(num>0):
        positives = positives+1
    else:
        negatives = negatives+1
print("Count the positive numbers entered: ",positives)
print("Count the Negative numbers entered: ",negatives)
print("Count the Zeroes entered: ",zeroes)
        