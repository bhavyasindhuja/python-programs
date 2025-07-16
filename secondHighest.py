arr=[1,5,22,7,24,3,57,65,99,98,120]
firsthighest=0
secondhighest=0
for i in range(len(arr)):
    if(arr[i]>secondhighest):
        if(arr[i]>firsthighest):
            secondhighest=firsthighest
            firsthighest=arr[i]
        else:
            secondhighest=arr[i]
print(secondhighest)