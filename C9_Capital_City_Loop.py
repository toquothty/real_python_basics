# Chapter 9 Challenge: Capital City Loop

import random

# Fill out a capitals dictionary with states/capitals
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

# Pick a random state and assign it to two variables
state, capital = random.choice(list(capitals_dict.items()))

# Display state, ask user to guess capital until correct, no case sensitive.
user_guess = input(f'The random state is: {state}, what is the capital: ')
user_guess = user_guess.lower()

# Display "Correct" on success and end, if user exits without guessing, display answer and "Goodbye"
while user_guess != capital.lower():
    user_guess = input(f'WRONG! Please try and guess the capital of {state} again. Othwerwise type exit to leave. ')
    user_guest = user_guess.lower()
    if user_guess == 'exit':
        exit()

if user_guess == capital.lower():
   print("Correct")
