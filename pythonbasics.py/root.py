# Solving Quadratic Equations
a = int(input("a value: "))
b = int(input("b value: "))
c = int(input("c value: "))

d =(b**2) - 4*a*c
root1 = (-b + (d**(1/2))) /2*a
root2 = (-b - (d**(1/2))) /2*a
print(f"Roots:({root1},{root2})")
