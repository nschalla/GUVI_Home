'''product of digit in number'''
n=int(input())
sum = 1
while (n > 0):
    sum = sum * int(n % 10)
    n = int(n / 10)

print(sum)