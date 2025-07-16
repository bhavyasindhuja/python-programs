n=int(input("Enter a number: "))
max=9
while(n>0):
    r=n%10
    n=n//10
    if(r<max):
        max=r
print(max)        
