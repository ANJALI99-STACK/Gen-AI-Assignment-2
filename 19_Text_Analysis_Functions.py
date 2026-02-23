#Count words
def count_words(text):
    words = text.split()
    return len(words)

#Count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

#Count consonants
def count_consonants(text):
    count = 0
    for ch in text:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count += 1
    return count

#Reverse text
def reverse_text(text):
    return text[::-1]

#Check palindrome
def is_palindrome(text):
    clean = ""
    for ch in text:
        if ch.isalnum():
            clean += ch.lower()
    return clean == clean[::-1]

#Remove vowels
def remove_vowels(text):
    result = ""
    for ch in text:
        if ch.lower() not in "aeiou":
            result += ch
    return result

#Word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

#Longest word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def analyze_text(text):
    print("\nTEXT ANALYSIS")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")
    print("Without vowels:", remove_vowels(text))
    long_word = longest_word(text)
    print("Longest word:", long_word, "(", len(long_word), "letters)")
    freq = word_frequency(text)
    print("Word Frequency:", end=" ")
    first = True
    for word in freq:
        if not first:
            print(",", end=" ")
        print(word + ":", freq[word], end="")
        first = False
    print()


text = input("Enter text: ")
analyze_text(text)