a=0
b=1

n=int(input("enter the number:"))
sum=0

sequence=[a,b]

for i in range(0,n-2):
    c=a + b
    a,b=b,c
    sequence.append(c)
for i in sequence:
    sum+=i
    
print(f"sequence is : {sequence}")
print(f"sum is :{sum}")