age = int(input("Enter the value: "))
day = input("Enter the day: ")
if age>=18 and day== "Wednesday":
    print("price=$10")
elif age>=18 and day!= "Wednesday" :
    print("price=$12")

if age<18 and day =="Wednesday":
    print("price=$6")
else:
    print("price=$8")
    
    

