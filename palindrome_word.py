word=input("enter your input:")

rev=""
for i in word:
    rev=i+rev

print("palindrome") if word==rev else print("not palindrome")