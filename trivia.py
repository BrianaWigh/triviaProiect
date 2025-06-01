import tkinter as tk

questions = [
    {
        "question": "Care este capitala Franței?",
        "choices": ["Paris", "Berlin", "Madrid", "Roma"],
        "answer": "Paris"
    },
    {
        "question": "Câte continente are Pământul?",
        "choices": ["5", "6", "7", "8"],
        "answer": "7"
    }
]
class TriviaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Game")
        self.current = 0
        self.score = 0
        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.load_question()
    def load_question(self):
        self.result_label.config(text="")
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        q = questions[self.current]
        self.question_label.config(text=q["question"])

        for choice in q["choices"]:
            btn = tk.Button(self.buttons_frame, text=choice, font=("Arial", 12), width=20,
                            command=lambda c=choice: self.check_answer(c))
            btn.pack(pady=5)
    def check_answer(self, selected):
        correct = questions[self.current]["answer"]
        if selected == correct:
            self.result_label.config(text=" Corect!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f" Greșit! Răspuns corect: {correct}", fg="red")

        self.current += 1
        if self.current < len(questions):
            self.root.after(1500, self.load_question)
        else:
            self.root.after(1500, self.show_final_score)
    def show_final_score(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        final = f"Scor final: {self.score} din {len(questions)}"
        tk.Label(self.root, text=final, font=("Arial", 20)).pack(pady=50)

root = tk.Tk()
app = TriviaGame(root)
root.mainloop()
