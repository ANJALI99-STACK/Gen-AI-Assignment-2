year = int(input("Enter a year: "))
#leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a LEAP year.")
    if year % 400 == 0:
        print("Reason: Divisible by 400.")
    else:
        print("Reason: Divisible by 4 and not divisible by 100.")
else:
    print(year, "is NOT a leap year.")
    if year % 4 != 0:
        print("Reason: Not divisible by 4.")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: Divisible by 100 but not by 400.")
        
    