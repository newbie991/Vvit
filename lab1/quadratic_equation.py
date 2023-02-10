print("ax^2+bx+c=0")

a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))

D=b**2-4*a*c

if D<0:
    print("Действительных реший нет")
elif D==0:
    x1 = (-b+D**0.5)/(2*a)
    print("x1={}".format(x1))
else:
    x1 = (-b+D**0.5)/(2*a)
    x2 = (-b-D**0.5)/(2*a)
    print("x1={}".format(x1))
    print("x1={}".format(x2))
