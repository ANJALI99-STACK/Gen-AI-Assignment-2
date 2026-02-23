#Factorial
def factorial(n):
    if n < 0:
        return "Not defined"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

#Prime Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#Fibonacc
def fibonacci(n):
    if n <= 0:
        return "Invalid"
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

#Sum of Digits
def sum_of_digits(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total

#Reverse Number
def reverse_number(n):
    rev = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return sign * rev

#Armstrong Number
def is_armstrong(n):
    num = abs(n)
    digits = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total == num

#GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

#Perfect Number
def is_perfect_number(n):
    if n <= 0:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def math_menu():
    while True:
        print("\n--- Mathematical Functions Menu ---")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 10:
            print("Exited")
            break

        elif choice == 1:
            n = int(input("Enter number: "))
            print("Result:", factorial(n))

        elif choice == 2:
            n = int(input("Enter number: "))
            print("Result:", is_prime(n))

        elif choice == 3:
            n = int(input("Enter term number: "))
            print("Result:", fibonacci(n))

        elif choice == 4:
            n = int(input("Enter number: "))
            print("Result:", sum_of_digits(n))

        elif choice == 5:
            n = int(input("Enter number: "))
            print("Result:", reverse_number(n))

        elif choice == 6:
            n = int(input("Enter number: "))
            print("Result:", is_armstrong(n))

        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", gcd(a, b))

        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", lcm(a, b))

        elif choice == 9:
            n = int(input("Enter number: "))
            print("Result:", is_perfect_number(n))

        else:
            print("Invalid choice")
math_menu()