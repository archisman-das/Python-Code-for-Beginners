a = int(input("Enter the marks for subject 1: "))
b = int(input("Enter the marks for subject 2: "))
c = int(input("Enter the marks for subject 3: "))
avg = (a+b+c)/3
if(avg>=90 and avg<=100):
    print("Grade-A")
elif(avg>=80 and avg<=89):
    print("Grade-B")
elif(avg>=70 and avg<=79):
    print("Grade-C")
elif(avg>=60 and avg<=69):
    print("Grade-D")
else:
    print("Grade-F")
