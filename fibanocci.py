n=int(input())
n1=0
n2=1
n3=0
if(n==1):
    print(0)
elif(n==2):
    print(0)
    print(1)
else:
    print(0)
    print(1)
    for i in range(n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)
       
  

