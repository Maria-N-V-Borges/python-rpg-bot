import random 

motivation_knowledge = {
    "sad": "Don't give up. Every programmer struggles sometimes. Keep going! 💪",
    "tired": "Take a short break and come back stronger. You are doing great! ☕",
    "difficult": "Learning programming takes time. Keep practicing! 🚀", 
    "error": "Errors are part of programming. They help you learn! 💻",
    "study": "Consistet study is the key to becoming a great programmer!"
}

general_messages = [
    "You are improving every day. Keep coding! 💻",
    "Every expert was once a beginner.",
    "Stay curious and keep learning!",
    "Programming is a journey, not a race."
]

def motivational_message():
    user_input = input("\n💬 Talk to the motivation bot: ").lower()

    for word in motivation_knowledge:
        if word in user_input:
            return motivation_knowledge[word]
        
    return random.choice(general_messages)