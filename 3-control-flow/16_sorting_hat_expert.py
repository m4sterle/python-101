import random

# Define a dictionary mapping answers to houses
answer_key = {
    1: ["Gryffindor", "Ravenclaw"],   # Dawn
    2: ["Hufflepuff", "Slytherin"],   # Dusk
    1: ["Gryffindor", "Hufflepuff"],  # The Good
    2: ["Slytherin", "Ravenclaw"],    # The Great 
    3: ["Ravenclaw", "Gryffindor"],   # The Wise
    4: ["Gryffindor", "Slytherin"],   # The Bold
    1: ["Gryffindor", "Ravenclaw"],   # Violin
    2: ["Slytherin", "Hufflepuff"],   # Trumpet
    3: ["Hufflepuff", "Ravenclaw"],   # Piano
    4: ["Gryffindor", "Slytherin"]    # Drum
}

# Define a dictionary to store house scores
house_scores = {
    "Gryffindor": 0,
    "Ravenclaw": 0,
    "Hufflepuff": 0,
    "Slytherin": 0
}

# Define a function to validate input and update scores
def update_score(question, answer):
    if answer in answer_key:
        houses = answer_key[answer]
        house_scores[houses[0]] += 1
        house_scores[houses[1]] += 1
        print(f"✔️ Option {answer} selected - {houses[0]} and {houses[1]} +1")
    else:
        print(f"⚠️ Invalid input for {question}. Skipping...")

# Sorting Ceremony
print("🎉 Welcome to the Sorting Ceremony! 🎉")
name = input("What's your name, young wizard? ")

print(f"\n🎩 Hmm... {name}, let's see where you belong! 🤔")

# Q1
print("\nQ1) Do you prefer:")
print("1) Dawn")
print("2) Dusk")
answer1 = int(input("Enter your choice (1 or 2): "))
update_score("Q1", answer1)

# Q2
qualities = ["The Good", "The Great", "The Wise", "The Bold"]
print(f"\nQ2) When I'm gone, I want people to remember me as:")
for i, quality in enumerate(qualities, 1):
    print(f"{i}) {quality}")
answer2 = int(input("Enter your choice (1-4): "))
update_score("Q2", answer2)

# Q3
instruments = ["Violin", "Trumpet", "Piano", "Drum"]
print(f"\nQ3) Which instrument most pleases your ear?")  
for i, instrument in enumerate(instruments, 1):
    print(f"{i}) The {instrument}")
answer3 = int(input("Enter your choice (1-4): "))
update_score("Q3", answer3)

# Determine the house with the highest score
sorted_house = max(house_scores, key=house_scores.get)

# Announce the sorting result with ASCII art
print(f"\n✨🎉💖 {name}, you belong in... {sorted_house}! 💖🎉✨")

if sorted_house == "Gryffindor":
    print("""
    🦁 Gryffindor 🦁
    ⚔️ Where dwell the brave at heart ⚔️
    💖 Their daring, nerve, and chivalry set Gryffindors apart! 💖
    """)
elif sorted_house == "Ravenclaw":
    print("""
    🦅 Ravenclaw 🦅 
    📚 Where those of wit and learning will always find their kind 📚
    💙 Wit beyond measure is man's greatest treasure! 💙
    """)  
elif sorted_house == "Hufflepuff":
    print("""
    🦡 Hufflepuff 🦡
    🌿 Where they are just and loyal, those patient Hufflepuffs are true 🌿
    💛 And unafraid of toil! 💛
    """)
else:
    print("""  
    🐍 Slytherin 🐍
    💚 Where you'll make your real friends, those cunning folk use any means 💚
    🌟 To achieve their ends! 🌟
    """)

print(f"\nCongratulations, {name}! 🎉 Your journey at Hogwarts begins! ✨🏰")