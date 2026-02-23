def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    else:
        return a / b
def modulus(a, b):
    return a % b
def power(a, b):
    return a ** b
def calculator():
    while True:
        print("\nCalculator")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. modulus")
        print("6. power")
        print("7. exit")
        choice = int(input("enter your choice: "))
        if choice == 7:
            print("exited")
            break
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
        if choice == 1:
            print("result:", add(a, b))
        elif choice == 2:
            print("result:", subtract(a, b))
        elif choice == 3:
            print("result:", multiply(a, b))
        elif choice == 4:
            print("result:", divide(a, b))
        elif choice == 5:
            print("result:", modulus(a, b))
        elif choice == 6:
            print("result:", power(a, b))
        else:
            print("invalid Choice")
calculator()