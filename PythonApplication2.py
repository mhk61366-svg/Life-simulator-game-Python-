def profile(user_info):
    print("\n--- Create Profile ---")
    name = input("Enter Your Name: ")
    age = input("Enter Age: ")
    user_info["Name"] = name
    user_info["Age"] = age
    return user_info

def Eating(energy,mood,hunger):
    print("\n--- Eating ---")
    print("The Food was Delicious")
    energy -= 15
    hunger -= 15
    return energy,mood,hunger

def sleep(energy,mood,hunger):
    print("\n--- Sleeping ---")
    print("Good night")
    energy += 15
    mood -= 15
    hunger += 15
    return energy,mood,hunger

def mini_game(energy,mood,hunger):
    print("\n--- Mini Game ---")
    x = 0
    print("Want to listen to a poem ")
    print("here you go ")
    print("")
    print("A world of logic, built in code")
    print("Where dreams and data intertwine and load")
    print("")
    print("Each loop a heartbeat, each line a spark")
    print("Awakening worlds from circuits dark.")
    print("")
    print("Press Start, and watch the silence break")
    print("As digital winds through numbers wake")
    print("")
    print("No maps are drawn, no rules are known")
    print("You shape the realm, the game’s your own")
    print("")
    print("Through bits and bytes, you find your way")
    print("A coder’s touch gives life its play")
    print("")
    print("So run the script, and let it be—")
    print("A simulation of your destiny.")
    print("")
    y = input("Want to read another poem (yes/no): ") # Add prompt for user input and clarify expected input
    if (y.lower() == "yes"): # Convert input to lowercase for case-insensitive comparison
        print("In realms of math and coded streams,")
        print("You craft the world that once was dreams.")
        print("")
        print("With keys and clicks, the laws are made,")
        print("Where light and logic softly fade.")
        print("")
        print("No chaos here—unless you choose,")
        print("For every path’s a code you’ll use.")
        print("")
        print("One function bends the course of fate,")
        print("A single loop decides the state.")
        print("")
        print("So play, creator, test your scheme,")
        print("Unfold the code that fuels the dream.")
        print("")
        print("This simulator—wild yet tame—")
        print("Awaits the hand that starts the game.")
        print("")
    else:
        print("Good Bye")
    
    energy -= 20
    mood += 20
    hunger += 20
    return energy,mood,hunger

def chatting(energy,mood,hunger):
    print("\n--- Chatting ---")
    print("Hello this is your AI bestie")
    AI_responses = {"hi":"Hello how are you doing","what is your favourite sports":"Tennis","which activity do you love":"singing poe
    response = "" # Initialize response
    while(response.lower() != "bye"): # Convert response to lowercase for case-insensitive comparison
        response = input("You: ") # Add prompt for user input
        if (response.lower() == "bye"): # Convert response to lowercase for case-insensitive comparison
            print("AI Bestie: Bye")
        elif response.lower() in AI_responses: # Check if response is in keys after converting to lowercase
            print("AI Bestie:", AI_responses.get(response.lower())) # Get response using lowercase key
        else:
            print("AI Bestie: I don't understand.") # Handle unrecognized input
            print("Chatting with you is fun and I learn alot of things")
        energy -= 15
        mood += 15
        hunger += 15
        return energy,mood,hunger

user_info = dict()
user_info = profile(user_info) # Assign the returned dictionary to user_infoenergy = 40mood = 40hunger = 40while (energy > 0 and mood > 0 and hunger < 100):
print("\n--- Main Menu ---")
print("What Do you Wish to Do?")
print("1. Send me to bed")
print("2. Chat with me")
print("3. Play a mini game")
print("4. Feed me")
print("5. View profile info")
print("6. View Attributes")
print("7. Exit")
try:
    choice = int(input("Enter your choice (1-7): ")) # Add prompt for user input
except ValueError: # Catch ValueError for non-integer input
    choice = -1
    if choice == 1:
        energy,mood,hunger = sleep(energy,mood,hunger)
    elif choice == 2:
        energy,mood,hunger = chatting(energy,mood,hunger)
    elif choice == 3:
        energy,mood,hunger = mini_game(energy,mood,hunger)
    elif choice == 4:
        energy,mood,hunger = Eating(energy,mood,hunger)
    elif choice == 5:
        print("\n--- Profile Info ---")
        print(user_info)
    elif choice == 6:
        print("\n--- Attributes ---")
        print("Energy:", energy)
        print("Mood:", mood)
        print("Hunger:", hunger)
    elif choice == 7:
        print("\n--- Exiting ---")
        print("Exiting the chatbot")
        print("")
    else:
        print("Good Bye")
        break

if (energy <= 0 or mood <= 0 or hunger >= 100):
print("\n--- Game Over ---")
print("Game Over")



