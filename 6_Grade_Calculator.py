s1 = int(input("Enter marks for Subject 1: "))
s2 = int(input("Enter marks for Subject 2: "))
s3 = int(input("Enter marks for Subject 3: "))
s4 = int(input("Enter marks for Subject 4: "))
s5 = int(input("Enter marks for Subject 5: "))
print("\nMarks in Each Subject:")
print("Subject 1:", s1)
print("Subject 2:", s2)
print("Subject 3:", s3)
print("Subject 4:", s4)
print("Subject 5:", s5)
total = s1 + s2 + s3 + s4 + s5
percentage = (total / 500) * 100

if s1 >= 40 and s2 >= 40 and s3 >= 40 and s4 >= 40 and s5 >= 40:
    result = "Pass"
else:
    result = "Fail"
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"
print("\nTotal Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)