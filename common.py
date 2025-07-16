var1="apple"
var2="batp"
var3="grapes"
ch='a'
for i in range(26):
    if(ch in var1 and ch in var2 and ch in var3):
        print(ch)
    ch=chr(ord(ch)+ 1)