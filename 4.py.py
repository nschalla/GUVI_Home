list = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    list.append(item)
for i in range(n):
    count=0
    for j in range(2,int(list[i]-1/2)):
        if(list[i]%j==0): 
            count+=1


    if(count==0):
         print(list[i],"is a prime number")
    else:
         print(list[i],"not a prime number")
