def small(num:list):
    smallest=num[0]

    for i in num:
        if smallest>i:
            smallest=i

    print(smallest)

n=[10,20,40,0,-1]

small(n)