def factorial(n):

    # Negative number case
    if n < 0:
        return "not defined"

    # 0 case
    if n == 0:
        return "0! = 1"

    fact = 1
    steps = ""
    for i in range(n, 0, -1):
        fact = fact * i
        steps += str(i)
        if i != 1:
            steps += " × "
    return str(n) + "! = " + steps + " = " + str(fact)


num = int(input("enter a number: "))
result = factorial(num)
print(result)