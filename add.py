a=int(input('enter a :'))
b=int(input('enter b :'))

operator=['+','-','/','*']
print(f"choose what you want to do from {operator}")

user_input=input()

if user_input=='+':
    print(a+b)
elif user_input=='-':
    print(a-b)
elif user_input=='*':
    print(a*b)
elif user_input=='/':
    print(a/b)
