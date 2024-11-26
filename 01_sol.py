age = int(input("Enter age: "))
if age<13:
    print("Child")
elif 13<=age<=19:
    print("Teenager")
elif 20<=age<=59:
    print("Adult")
else:
    print("Senior")