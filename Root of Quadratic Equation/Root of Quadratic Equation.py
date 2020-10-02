import math

print("Assuming Quadratic Equation of for ax^2+bx+c")
a,b,c = map(float,input("Please enter a,b and c ==> ").split())

d = (b**2) - (4*a*c)

if d<0:
    print("Roots are Imaginary")
elif d==0:
    r = -b / (2*a)
    print("Roots of Quadratic Equation are ==> ",r)
else:
    r1 = ((-b) + math.sqrt(d)) / (2*a)
    r2 = ((-b) - math.sqrt(d)) / (2*a)
    print("Roots of Quadratic Equation are ==> ",r1,r2)