# Write code below 💖

import random

# List of possible answers from the Magic 8 Ball
answers = [
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.", 
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Get the user's question 
question = input("Question: ")

# Select a random answer from the list
answer = random.choice(answers)

# Print the question and the Magic 8 Ball's answer
print("Question:", question)
print("Magic 8 Ball:", answer)

# This line imports the random module, which provides functions for generating random numbers and making random selections.

# This is a list that contains the possible answers from the Magic 8 Ball. Each answer is a string enclosed in quotes.

# The input() function prompts the user to enter a question and stores it in the 'question' variable.

# The random.choice() function selects a random answer from the 'answers' list and assigns it to the 'answer' variable.

# These lines print the user's question and the randomly selected answer from the Magic 8 Ball.