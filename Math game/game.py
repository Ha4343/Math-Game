import random
import time
from ui import show_question, show_result

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*", "/"])
    
    if operation == "/":
        num1 = num2 * random.randint(1, 5)  # Ensure division is clean
    
    question = f"{num1} {operation} {num2}"
    answer = eval(question)  # Calculate answer
    return question, round(answer, 2) if operation == "/" else answer

def play_game():
    score = 0
    for _ in range(5):  # 5 rounds
        question, correct_answer = generate_question()
        start_time = time.time()
        
        user_answer = show_question(question)
        elapsed_time = time.time() - start_time

        if elapsed_time > 5:
            show_result("⏳ Time's up!", score)
            break
        elif user_answer == str(correct_answer):
            score += 1
            show_result("✅ Correct!", score)
        else:
            show_result(f"❌ Wrong! Correct answer: {correct_answer}", score)

    print("\n🎉 Game Over! Your final score:", score)

if __name__ == "__main__":
    play_game()
