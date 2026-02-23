def c_to_f(c):
    return (c * 9/5) + 32
def f_to_c(f):
    return (f - 32) * 5/9
def c_to_k(c):
    return c + 273.15
def k_to_c(k):
    return k - 273.15
def f_to_k(f):
    return (f - 32) * 5/9 + 273.15
def k_to_f(k):
    return (k - 273.15) * 9/5 + 32
def temperature_converter():
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 7:
            print("exited")
            break
        temp = float(input("Enter temperature: "))
        if choice == 1:
            print("Result:", round(c_to_f(temp), 2), "°F")

        elif choice == 2:
            print("Result:", round(f_to_c(temp), 2), "°C")

        elif choice == 3:
            print("Result:", round(c_to_k(temp), 2), "K")

        elif choice == 4:
            print("Result:", round(k_to_c(temp), 2), "°C")

        elif choice == 5:
            print("Result:", round(f_to_k(temp), 2), "K")

        elif choice == 6:
            print("Result:", round(k_to_f(temp), 2), "°F")
        else:
            print("invalid choice")
temperature_converter()