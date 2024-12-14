import random

def number_guessing_game():
    print("Welcome to The number Guessing game !")
    
    # Generate a random number between 1 and 100

    secret_number = random.randint(1,100)

    attempts = 0
    while True:
        try:

            # Ask user for their guess

            guess = int(input("Guess a number between 1 to 100 : "))

            attempts +=1
            # Check if the guess is too low, too high, or correct

            if guess < secret_number:
                print("Too low ! Try again . ")
        
            elif guess > secret_number:
                print("Too high ! Try again . ")
        
            else:
                print(f"congratulations ! you've guesss the number {secret_number} correctly in {attempts} attempts")
                break
        except ValueError:
                print("please enter a valid number .")
    
        if __name__== "__main__":
                number_guessing_game()
    
    