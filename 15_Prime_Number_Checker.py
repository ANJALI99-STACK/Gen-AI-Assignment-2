def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f" {num} is a prime Number")
else:
    print(f"{num} is not a prime Number")


start = int(input("enter start range: "))
end = int(input("enter end range: "))
print("prime numbers:", end=" ")
primes = []
for i in range(start, end + 1):
    if is_prime(i):
        primes.append(str(i))
print(", ".join(primes))