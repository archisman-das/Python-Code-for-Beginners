call = int(input("Enter the number of calls: "))
if(call<=100):
    print("Monthly Telephone Bill is: ",amount=200)
elif(call>100 and call<=150):
    call = call-100
    amount = 200+(0.60*call)
    print("Monthly Telephone Bill is:",amount)
elif(call>150 and call<=200):
    call = call-150
    amount = 200+(0.60*50)+(0.50*call)
    print("Monthly Telephone Bill is:",amount)
else:
    call = call-200
    amount = 200+(0.60*50)+(0.50*50)+(0.40*call)
    print("Monthly Telephone Bill is:",amount)

