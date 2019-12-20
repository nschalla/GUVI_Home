def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
a=int(input("enter the first number"))
b=int(input("enter  the second number"))
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
c=int(input("enter the choice"))
if c==1:
    print("addition ",a,"+",b,"=",add(a,b))
elif c==2:
    print("Subtraction",a,"-",b,"=",sub(a,b))
elif c == 3:
    print("mutilpliaction", a,"*", b, "=", mul(a, b))
elif c==4:
    print("division",a,"/",b,"=",div(a,b))
else:
    print("please enter correct operator")


