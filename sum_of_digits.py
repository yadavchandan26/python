#Find the sum of digits of a number

num=int(input("enter the number:"))
print(f"Your entered number is : {num}")

digit_group=[]
i=0
while i<num:
    digit=num%10
    digit_group.append(digit)
    num=num//10



sum=0
for val in digit_group:
    sum+=val

print(f"The sum of all the digit from {num} will be :{sum}")