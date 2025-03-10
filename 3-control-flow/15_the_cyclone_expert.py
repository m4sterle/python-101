# The Cyclone 🎢
# Codédex

 # Get user input for height (in cm) and credits
height = int(input("Enter your height (in cm): "))
credits = int(input("Enter your credit count: "))

# Check if user meets both height and credit requirements
if height >= 137 and credits >= 10:
    print("Congratulations! You meet all requirements for the ride. Enjoy your adventure! 🎢🏰")
else:
    # Create a list to store the reasons for not meeting requirements
    reasons = []
    
    # Check if height is below the requirement
    if height < 137:
        reasons.append("height")
    
    # Check if credits are below the requirement 
    if credits < 10:
        reasons.append("credits")
    
    # Print a personalized message based on the missing requirements
    if len(reasons) == 1:
        print(f"Oops! You don't meet the {reasons[0]} requirement. Keep leveling up! 💪")
    else:
        print(f"Oops! You don't meet the {' and '.join(reasons)} requirements. Keep leveling up! 💪")
