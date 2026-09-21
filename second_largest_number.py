num=[]

n=int(input("enter how many numbers do you want to insert:"))

for i in range(n):
    val=int(input("enter the value:"))
    num.append(val)

print(f"number list is : {num}")

large=0

for j in num:
    if j>large:
        large=j

if large in num:
    num.remove(large)

second_large=0

for k in num:
    if k>second_large:
        second_large=k

print(f"second largest number is:{second_large}")