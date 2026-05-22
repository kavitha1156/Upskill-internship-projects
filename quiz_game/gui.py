import tkinter as tk
from quiz.loader import load_questions
from quiz.quiz_logic import QuizGame

questions = load_questions("data/questions.json")
quiz = QuizGame(questions)

root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x400")

question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
question_label.pack(pady=20)

selected_option = tk.StringVar()

def load_question():
    if quiz.has_next():
        q = quiz.get_question()
        question_label.config(text=q["question"])

        selected_option.set(None)

        for i, option in enumerate(q["options"]):
            buttons[i].config(text=option, value=option)
    else:
        question_label.config(text=f"Final Score: {quiz.get_score()}")
        for btn in buttons:
            btn.pack_forget()

def next_question():
    quiz.check_answer(selected_option.get())
    load_question()

buttons = []
for _ in range(4):
    btn = tk.Radiobutton(root, text="", variable=selected_option, value="")
    btn.pack(anchor="w")
    buttons.append(btn)

next_btn = tk.Button(root, text="Next", command=next_question)
next_btn.pack(pady=20)

load_question()

root.mainloop()