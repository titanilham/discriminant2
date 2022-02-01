a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = ( b**2 - 4*a*c )
d2 = d ** 0.5

x1 = b* -1 + d2
x11 = (x1 / 2*a)
x2 = b* -1 - d2
x22 = (x2 / 2*a)
if d == 0:
    print ("x1= ", x11 )
elif d < 0:
    print("нет корней")
else:
    print ("x1= ", x11 )
    print("x2= ", x22 )

