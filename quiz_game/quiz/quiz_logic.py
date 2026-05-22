class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current = 0

    def has_next(self):
        return self.current < len(self.questions)

    def get_question(self):
        return self.questions[self.current]

    def check_answer(self, answer):
        correct = self.questions[self.current]["answer"]

        if answer == correct:
            self.score += 1

        self.current += 1

    def get_score(self):
        return self.score