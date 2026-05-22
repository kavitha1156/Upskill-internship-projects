import tkinter as tk
from tkinter import messagebox

# 🔹 Quiz Data (you can later move this to JSON)
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is don't have oop concept?",
        "options": ["Java", "C++", "Python", "HTML"],
        "answer": "HTML"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]

# 🔹 Quiz Class (Logic + Score)
class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.index = 0
        self.score = 0

    def current_question(self):
        return self.questions[self.index]

    def check_answer(self, selected):
        correct = self.questions[self.index]["answer"]
        if selected == correct:
            self.score += 1
        self.index += 1

    def has_next(self):
        return self.index < len(self.questions)


# 🔹 Initialize Quiz
quiz = QuizGame(questions)

# 🔹 Create Window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x400")

# 🔹 Variables
selected_option = tk.StringVar()

# 🔹 UI Elements
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=selected_option, value="", font=("Arial", 12))
    btn.pack(anchor="w", padx=20)
    option_buttons.append(btn)


# 🔹 Load Question
def load_question():
    if quiz.has_next():
        q = quiz.current_question()
        question_label.config(text=q["question"])
        selected_option.set(None)

        for i, option in enumerate(q["options"]):
            option_buttons[i].config(text=option, value=option)
    else:
        show_result()


# 🔹 Next Button Logic (CORE PART)
def next_question():
    selected = selected_option.get()

    if not selected:
        messagebox.showwarning("Warning", "Please select an option!")
        return

    # 👉 Collect answer and update score
    quiz.check_answer(selected)

    # 👉 Load next question
    load_question()


# 🔹 Show Final Score
def show_result():
    question_label.config(text=f"Final Score: {quiz.score} / {len(questions)}")

    for btn in option_buttons:
        btn.pack_forget()

    next_btn.pack_forget()


# 🔹 Button
next_btn = tk.Button(root, text="Next", command=next_question, bg="green", fg="white")
next_btn.pack(pady=20)

# 🔹 Start Quiz
load_question()

# 🔹 Run App
root.mainloop()