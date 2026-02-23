a = float(input("enter first number: "))
b = float(input("enter second number: "))
add = a + b
sub = a - b
mul = a * b
if b != 0:
    div = a / b
else:
    div = "Undefined (Division by Zero)"
mod = a % b
power = a ** b
print("\nresults:")
print(a, "+", b, "=", add)
print(a, "-", b, "=", sub)
print(a, "*", b, "=", mul)
print(a, "/", b, "=", round(div, 2) if b != 0 else div)
print(a, "%", b, "=", mod)
print(a, "^", b, "=", power)