from quiz.loader import load_questions
from quiz.quiz_logic import QuizGame

def main():
    questions = load_questions("data/questions.json")
    quiz = QuizGame(questions)

    print("Quiz Game")
    print("-------------------")

    while quiz.has_next():
        q = quiz.get_question()

        print("\n" + q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        choice = int(input("Enter option number: "))
        selected = q["options"][choice - 1]

        quiz.check_answer(selected)

    print("\nFinal Score:", quiz.get_score(), "/", len(questions))


if __name__ == "__main__":
    main()