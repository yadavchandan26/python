#prime number is that number which does not come in any number's table except of its owm

num=int(input("enter the number :"))

for i in range(2,num):
    if num%i==0:
        print("not a prime number")
        break
else:
    print("prime number")