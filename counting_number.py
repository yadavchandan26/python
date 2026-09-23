#Count how many times each number occurs in a list

num=[10,20,30,40,20,30]
seen=[]
for i in num:
    if i not in seen:
        print(i,num.count(i))
        seen.append(i)
