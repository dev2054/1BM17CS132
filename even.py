list=[]
numbers=int(input("enter the list length"))
print("enter numbers")
for i in range(numbers):
    data=int(input())
    list.append(data)
print(list)

b=[j for j in list
    if j%2==0
       ]
print(b)
        
