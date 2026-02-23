#Pattern 1
def pattern1(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

#Pattern 2
def pattern2(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

#Pattern 3
def pattern3(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

#Pattern 4
def pattern4(n):
    for i in range(1, n + 1):
        #spaces
        for space in range(n - i):
            print(" ", end="")

        for j in range(1, i + 1):
            print(j, end="")

        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()


#3 MORE CREATIVE PATTERNS
#Pattern 5: Star Triangle
def pattern5(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

#Pattern 6: Inverted Star Triangle
def pattern6(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

#Pattern 7: Number Square
def pattern7(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

def pattern_menu():

    while True:
        print("\n--- Pattern Generator Menu ---")
        print("1. pattern 1")
        print("2. pattern 2")
        print("3. pattern 3")
        print("4. pattern 4")
        print("5. pattern 5")
        print("6. pattern 6")
        print("7. pattern 7")
        print("8. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 8:
            print("Exited")
            break
        height = int(input("Enter height: "))
        if choice == 1:
            pattern1(height)
        elif choice == 2:
            pattern2(height)
        elif choice == 3:
            pattern3(height)
        elif choice == 4:
            pattern4(height)
        elif choice == 5:
            pattern5(height)
        elif choice == 6:
            pattern6(height)
        elif choice == 7:
            pattern7(height)
        else:
            print("Invalid")

pattern_menu()