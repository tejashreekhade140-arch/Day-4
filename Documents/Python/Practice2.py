#print table of odd numbers from 1 to 10
n=10
for i in range(1,11,2):
    for j in range(1,11):
        print(i*j)

#create a heterogenous list of numbers and names.Split the list from highest number
list=[1,"Tejashree",2,"Soummya",3,4,5,"Ankita","Priti",]
number=[i for i in list if type(i)==int]
high=max(number)
split_p=list.index(high)

first_part=list[:split_p+1]
second_part=list[split_p+1:]

print("First Part:", first_part)
print("Second Part:", second_part)

#Accept the name and Check if its Palindrome.
name=input("Enter your Name:")
p_name=name.lower()
if name==p_name[::-1]:
    print(f"Yes, '{name}',is a Palindrone")
else:
    print(f"No, '{name}',is not a Palindrome")


#print the sum of digits
num=input("Enter a Number:")
sum=0
for i in num:
        sum+=int(i)
print(f"The sum of Digit is : {sum}")

#print the sum of digits without String fuction
#num=input("Enter a Number:")
#d_sum=0
#while num>0:
 #   digit=num% 10
 #   d_sum+=digit
 #   num=num//10
#print(d_sum)

#print Following patterns
#*
##
#***
for i in range(1,5):
    if i%2!=0:
        print("*"*i)
    else:
        print("#"*i)

#pyramid
for i in range(1,6):
        print("*"*i)
    
        
#add two numbers at third position of list and append one nmae in list and then split

