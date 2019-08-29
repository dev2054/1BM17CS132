
list=[]
numbers=int(input("enter the list length"))
print("enter numbers")
for i in range(numbers):
    data=int(input())
    list.append(data)
print(list)
number=int(input("enter the element to be searched")) 

if number== numbers:
  print(number, "is present")
else:
  print(number, "isnot present")
  

