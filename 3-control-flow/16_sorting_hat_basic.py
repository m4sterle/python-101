name = input("What is your name? ")

print(f"Hmm... {name}, let's see where you belong!")

# Initialize the house variables with a starting score of 0
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

answer1 = input("Q1) Do you like Dawn or Dusk? ")

if answer1 == "Dawn":
    print("Ah, an early riser! ⛅")
    gryffindor += 1
    ravenclaw += 1
elif answer1 == "Dusk":
    print("Ooh, a night owl! 🌙")
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input! ⚠️")


# ... (repeat for Q2 and Q3)

print(f"\nHere are the results for {name}:")
print("Gryffindor:", gryffindor)
print("Ravenclaw:", ravenclaw) 
print("Hufflepuff:", hufflepuff)
print("Slytherin:", slytherin)

house = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if house == gryffindor:
    print(f"\n{name}, you belong in... Gryffindor! 🦁")
elif house == ravenclaw:
    print(f"\n{name}, you belong in... Ravenclaw! 🦅")
elif house == hufflepuff:
    print(f"\n{name}, you belong in... Hufflepuff! 🦡")
else:
    print(f"\n{name}, you belong in... Slytherin! 🐍")


