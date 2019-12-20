'''to check  the given number is palindrome or not'''
n=int(input())
num=n
sum=0
while(num!=0):
    re=int(num%10)
    sum=sum*10+re
    num=int(num/10)
if (n==sum):
    print(sum,"is a palidrome")
else:
    print(n,"is not a palidrome")