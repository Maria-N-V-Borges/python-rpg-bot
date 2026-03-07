score = 10

def add_points(points):
    global score
    score += points
    print(f"🏆 You gained {points} points!")

def remove_points(points):
    global score
    score -= points
    print(f"⚠️ You lost {points} points")

def show_score():
    return score