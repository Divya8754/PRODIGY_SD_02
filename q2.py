import random

def play_game():

    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10 
    
    print("Welcome to the Number Guessing Game!")
    print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return attempts 
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
    return max_attempts  

def main():
    score = 0
    rounds_played = 0
    play_again = "Y"

    while play_again.upper() == "Y":
        rounds_played += 1
        print(f"\nRound {rounds_played}:")

        attempts = play_game()
        score += attempts
    
        play_again = input("Do you want to play again? (Y/N): ")
    
    print(f"\nGame Over! You played {rounds_played} round(s) with a total score of {score}.")
    print(f"Your average attempts per round: {score / rounds_played:.2f}")
main()