string="hdasbcassj"
arr=[0]*26
for i in range(len(string)):
    arr[ord(string[i])-97]+=1

for i in range(len(arr)):
    print(chr(i+97), "->",arr[i])