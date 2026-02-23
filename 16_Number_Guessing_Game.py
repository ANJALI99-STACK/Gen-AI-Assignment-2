import random
def play_game(best_score):
    number = random.randint(1, 100)
    attempts = 7
    used = 0
    print("\nguess a number between 1 and 100.")
    print("you have 7 attempts. Try to guess it")
    while attempts > 0:
        guess = int(input("enter your guess: "))
        used += 1
        attempts -= 1
        if guess == number:
            print("congratulations, you guessed it right.")
            print("attempts used:", used)
            if best_score is None or used < best_score:
                best_score = used
                print(" new Best Score")
            return best_score
        if abs(guess - number) <= 5:
            print("you are very close")
        if guess > number:
            print("too High")
        else:
            print("too Low")
        print("attempts remaining:", attempts)
    print("\ngame Over!")
    print("the number was:", number)
    return best_score
best_score = None
while True:
    best_score = play_game(best_score)
    print("\nbest Score:", best_score)
    again = input("play again? (yes/no): ")
    if again.lower() != "yes":
        print("Ttanks for playing!")
        break