def learn_programming():
    print("\n📚 Programming Assistant")
    print("Ask me something about programming!")
    print("Type 'exit' to go back to the menu.\n")

    knowledge = {
        "python": "Python is a powerful language used for AI, automation, and web development.",
        "html": "HTML is a markup language used to structure web pages.", 
        "css": "CSS is used to style web pages.",
        "javascript": "JavaScript adds interactivity to websites.",
        "git": "Git is a version control system used to track code changes.",
        "github": "Github is a platform where developers store and share code repositories.",
        "algorithm": "An algorithm is a step-by-step procedure tosolve a problem.",
        "variable": "A variable store data that can b used later in a program"
    }

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Returning to the main menu...\n")
            break

        found = False

        for word in knowledge:
            if word in user_input:
                print("Bot:", knowledge[word])
                found = True
                break
        
        if not found:
            print("Bot: I'm still learning about that topic")