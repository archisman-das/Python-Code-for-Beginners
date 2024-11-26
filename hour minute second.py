seconds = int(input("Enter the Seconds: "))
hour = seconds//3600
minutes = (seconds%3600)//60
second = (seconds%3600)%60
print("Hour = ",hour)
print("Minutes = ",minutes)
print("Secons = ",second)