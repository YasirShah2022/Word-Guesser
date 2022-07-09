print("Welcome to the game of hangman!")

# variable to store the secret word
secret = "BUBBLES"

# Creating a variable that will be counted inside the funtion
global count
count = 1

# create a variable to count the length of the secret word
lengthSecret = len(secret)

# Create a blank list to match the length of the secret word and hold user guesses
userGuess = []
for _ in range(lengthSecret):
    userGuess.append("_")



  
# Funtion to display and check the user guesses
def guessCheck():
  # Create a single char variable so the while loop for the prompt can be initiated
  guess = ""
  # importing the global variable to count the attempts
  global count
  # Creating a variable to track the iterations for indexing the user guess
  index = -1
  print()
  # Creat a while loop to check if the user only entered a single letter
  while (len(guess) != 1):
    # Create a prompt fot he user to enter a single letter for the guesses, case insensitive
    guess = input("Enter a single letter: ")
  guess = guess.upper()
  
  # Check if the guessed letter is not secret word and count an attempt
  if guess not in secret:
    count += 1
    print(f"{guess} is not in the secret word, you have {7 - count} attempts left.")
    
  # Loop through the secret word and see if the guess is at any of the indices  
  for letter in secret:
    index += 1
    
    if guess == letter:
      userGuess.pop(index)
      userGuess.insert(index,letter)
  
  guessedWord =""
  for letter in userGuess:
    guessedWord += letter
  print(f'Your guess: {guessedWord}')
  return guessedWord



  
                  ## Main program code block ##
# continue game if the userGuess is not equal to secret and attempts left 
gameContinue = True    
# Run game if with in the six tries
while gameContinue:
  # Run the game funtion if the game continue conditions are met
  guessedWord = guessCheck()
  # Check if number of attempts is less than 6 
  if (guessedWord == secret) and (count < 6):
    gameContinue = False
    print("You guessed it correctly, you won!")
  elif count > 6:
    gameContinue = False
    print("You ran out of turns without guessing the correct word.")

      
  

 



































# Create a string variable to store user guesses 
  
  
# Create a function that determines if the user has won the game
# (the algorithm for that function is in another hint, if you're struggling with it)
 
# Create the secret word
 
# Setup a collection to store user guesses
 
# Setup a variable to hold the number of strikes the user receives
 
# If the user has NOT won OR lost, take a turn
 
  # Get a SINGLE letter from the user
 
  # Store the guess
 
  # Determine if this letter is in the secret word
 
  # If it is, display the secret word with all of our current guesses
 
  # If it isn't, give the user a strike and tell them that the letter is an incorrect guess
 
# If the user lost, display that message
 
# If the user won, display that message, and the entire secret word