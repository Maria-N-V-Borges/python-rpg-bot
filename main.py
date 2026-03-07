from chatbot import learn_programming 
from questions import programming_challenge
from motivation import motivational_message
from score import show_score

print("🤖 Welcome to Python RPG Bot!")
print("Your journey to becoming a programmer starts now! 🚀")

while True:
    print("\n======= MAIN MENU =========")
    print("1 - Learn Programming")
    print("2 - Programming challenge")
    print("3 - View score")
    print("4 - Motivation")
    print("5 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        learn_programming()
    
    elif choice == "2":
        programming_challenge()

    elif choice == "3":
        print("🏆 Your score:", show_score())

    elif choice == "4":
        print(motivational_message())

    elif choice == "5":
        print("See you next time, programmer! 💻✨")
        break

    else:
        print("Invalid option. Please try again")