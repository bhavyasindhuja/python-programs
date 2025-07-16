n=6

if(n%2==0):
    value1=n//2
    value2=value1-1
else:
    value1=n//2
    value2=n//2


for i in range(n):
    for j in range(n):
        if(j==value1 or j==value2):
            print("$",end=" ")
        elif i==0 or i==n-1 or j==0 or j==n-1:
            print ("*",end=" ")
        else:
            print(" ",end=" ")
    print()
