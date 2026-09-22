#Find the common elements between two lists

list_1=[]
list_2=[]

for i in range(5):
    val=int(input("enter value for list 1:"))
    list_1.append(val)
print("list 1 elements are :",list_1)

for j in range(5):
    vals=int(input("enter value for list 2:"))
    list_2.append(vals)

print("list 2 elements are :",list_2)
common_element=[]

for i in list_1:
    if i in list_2:
        common_element.append(i)


print("common elements are:",common_element)