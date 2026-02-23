n = int(input("How many numbers? "))
total = 0
numbers = []
for i in range(1, n + 1):
    num = int(input("Enter number " + str(i) + ": "))
    numbers.append(num)
    total = total + num

#average
average = total / n
#maximum and minimum
maximum = max(numbers)
minimum = min(numbers)

#results
print("\nSum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)