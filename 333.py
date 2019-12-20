n=int(input("enter the number"))
sum = 0
while (num > 0):
    sum += int(n % 10)
    n = int(n / 10)
print(sum)

