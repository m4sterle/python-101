#!/usr/bin/env python3

# 🔮✨ Magic 8 Ball Fortune Teller ✨🔮

import random  # 🎲 Summoning the power of randomness! 

# 🗝️ Defining the sacred scroll of possible answers 📜✨
answers = [
    "It is certain.",                  # 🍃 Farore's Wind of Courage
    "Without a doubt.",                # 🔥 Din's Fire of Power
    "You may rely on it.",             # 💧 Nayru's Love of Wisdom
    "Yes, definitely.",                # 🌿 Saria's Song of Friendship
    "It is decidedly so.",             # ⭐ Star Fragments of Truth
    "As I see it, yes.",               # 👀 Lens of Truth
    "Most likely.",                    # 🌞 Sun's Song of Hope
    "Yes.",                            # ✅ Affirmative!
    "Outlook good.",                   # 🔮 Positive Prophecy
    "Signs point to yes.",             # 🎚️ Sheikah Sensor Says Yes!
    "Reply hazy, try again.",          # 🌫️ Fog of Uncertainty
    "Ask again later.",                # ⏳ Sands of Time Still Shifting
    "Better not tell you now.",        # 🙊 Sheikah Secret
    "Cannot predict now.",             # 🤷 Unclear Destiny
    "Concentrate and ask again.",      # 🧘 Meditate on Your Question
    "Don't count on it.",              # ❌ Doubtful Destiny
    "Outlook not so good.",            # 🌑 Moon's Foreshadowing
    "My sources say no.",              # 🧚‍♂️ Fairies' Whispers of Warning 
    "Very doubtful.",                  # 🌋 Deku Tree's Lament
    "No."                              # 🛑 Negative.
]

# 🔁 Main program loop (like exploring a dungeon!) 🗡️🛡️
while True:
    # ❓ Prompting the user for a question (like playing the Ocarina!)
    question = input("❓ Ask the Magic 8 Ball a Yes/No question (or press Enter to quit): ")
    
    # 🚪 Giving the user a way out of the loop (like using the Door of Time)
    if question == "":
        break
    
    # 🔮 Selecting a random answer (like drawing a rune from the Goddess!)
    answer = random.choice(answers)
    
    # 💬 Printing the question and answer with proper formatting (like the Sign of the Triforce!)
    print(f"\nQuestion: 🤔 {question}")
    print(f"Magic 8 Ball: 🔮✨ {answer}\n")

# 🌟 Printing a fond farewell (like Navi flying away)
print("May the Triforce guide your path! 💙❤️💚 Until next time!")