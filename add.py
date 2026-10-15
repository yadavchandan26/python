a=int(input('enter a :'))
b=int(input('enter b :'))

operator=['+','-','/','*']
print(f"choose what you want to do from {operator}")

user_input=input(f'you choose:')

if user_input=='+':
    print(a+b)
elif user_input=='-':
    print(a-b)
elif user_input=='*':
    print(a*b)
elif user_input=='/':
    print(a/b)
else:
    print(f'choose correct from {operator}')