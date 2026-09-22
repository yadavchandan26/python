#Remove duplicate values from a list without using set()

num=[]
n=int(input("enter your input number(how many):"))
for val in range(n):
    val=int(input("enter your value:"))
    num.append(val)

unique=[]

for i in num:
    if i not in unique:
        unique.append(i)

print(f"list is: {num}")
print(f"all unique numbers are: {unique}")
print(f"without using set()")