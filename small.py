arr1=[1,2,3,55]
arr2=[5,9,54,125,345]
min=100000000
temp=0
for i in range(len(arr2)):
    for j in range(len(arr1)):
        temp=arr2[i]-arr1[j]
        if(temp<min and temp>=0):
            min=temp
print(min)