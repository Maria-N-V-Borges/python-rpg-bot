import random
from score import add_points, remove_points
from motivation import motivational_message

questions = [
    {
        "question": "What does HTML stand for?", 
        "options": {
            "A": "Hyper Trainer Marking Language",
            "B": "Hyper Text Markup Language",
            "C": "High Text Machie Language"
        },
        "answer": "B"
    },
    {
        "question": "Which language is widely used for Artificial Intelligence?",
        "options": {
            "A": "Python",
            "B": "HTML",
            "C": "CSS"
        },
        "answer": "A"
    },
    {
        "question": "What is Git mainly used for?",
        "options": {
            "A": "Design websites",
            "B": "Version control",
            "C": "Create databases"
        },
        "answer": "B"
    }
]

def programming_challenge():
    print("\n🎮 Programming Challenge!")

    question = random.choice(questions)

    print("\n" + question["question"])

    for key, value in question["options"].items():
        print(f"{key}) {value}")

    user_answer = input("Your answer: ").upper()

    if user_answer == question["answer"]:
        print("🎉 Correct! Well done!")
        add_points(5)
    else:
        print("❌ that's not correct.")
        print("Correct answer:", question["answer"])
        remove_points(2)
        print(motivational_message())