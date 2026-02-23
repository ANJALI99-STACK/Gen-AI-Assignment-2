def check_palindrome(text):
    original = text
    lower_text = text.lower()     # Ignore case
    reversed_text = lower_text[::-1]   # Reverse string

    print("\nOriginal:", original)
    print("Reversed:", reversed_text)
    if lower_text == reversed_text:
        return "PALINDROME"
    else:
        return "NOT A PALINDROME"

value = input("Enter word/number: ")
result = check_palindrome(value)
print("Result:", result)