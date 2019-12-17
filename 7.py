n = int(input("Enter the number of units: "))
amount=0
if(n<50):
    amount=n*45
    print("Amount need to be paid:",amount)
elif(n<100):
    amount=n*55
    print("Amount need to be paid:",amount)
elif(n<200):
    amount=n*75
    print("Amount need to be paid:",amount)
else:
    amount=n*85
    print("Amount need to be paid:",amount)