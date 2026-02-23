#Single Number Table
num = int(input("Enter number: "))
end = int(input("Enter range: "))
print("\nMultiplication Table of", num)
for i in range(1, end + 1):
    print(num, "x", i, "=", num * i)

#Full Multiplication Table (1 to 10)
print("\n--- Full Multiplication Table (1 to 10) ---\n")

for i in range(1, 11):
    for j in range(1, 11):
        print(str(i * j).ljust(4), end=" ")
    print()