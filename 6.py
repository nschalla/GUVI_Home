list = []
n = int(input("Enter the number of subject"))
for i in range(n):
    print("subject",i+1,":")
    item = int(input())
    list.append(item)
for i in range(n):   
    if(list[i]>=91):
        print("subject",i+1," is A+")
    elif(list[i]>=75):
        print("subject",i+1," is B")
    elif(list[i]>=60):
        print("subject",i+1,"is C")
    else:
        print("subject",i+1," is D")