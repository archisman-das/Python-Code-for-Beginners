range1=int(input("Enter Range1="))
range2 = int(input("Enter Range2="))
for i in range(range1,range2+1):
   if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        
        else:
            print(i,end=" ")
        
        