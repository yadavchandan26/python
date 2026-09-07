# fibonacci sequence


#we all know that fibonacci serie start with 0,1 and keep goes until they met n

a=0 #the first number which is zero
b=1 #the second number which is 1

#now all depends on n and this two numbers

n=int(input("enter the number:"))

fibo_sequence=[0,1]
for i in range(n-2): # -2 because we already knew the first two number and even already included in the list
    c=a+b
    fibo_sequence.append(c)
    a,b=b,c

fibo_sequence
