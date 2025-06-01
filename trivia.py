import tkinter as tk
#Lista cu intrebari este un dictionar
questions = [
    {
        "question": "În ce an s-a lansat Python?",
        "choices": ["1989", "1991", "1995", "2000"],
        "answer": "1991"
    },
    {
        "question": "Cine a creat limbajul Python?",
        "choices": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Linus Torvalds"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Ce tip de fișier are extensia specifică Python?",
        "choices": [".py", ".js", ".java", ".cpp"],
        "answer": ".py"
    },
    {
        "question": "Ce funcție este folosită pentru a afișa text pe ecran?",
        "choices": ["echo()", "print()", "show()", "write()"],
        "answer": "print()"
    },
    {
        "question": "Ce cuvânt cheie definește o funcție în Python?",
        "choices": ["func", "function", "def", "define"],
        "answer": "def"
    },
    {
        "question": "Cum declari o listă goală în Python?",
        "choices": ["[]", "{}", "()", "null"],
        "answer": "[]"
    },
    {
        "question": "Ce valoare booleană reprezintă fals în Python?",
        "choices": ["false", "False", "0", "none"],
        "answer": "False"
    },
    {
        "question": "Cum se numește biblioteca standard pentru interfață grafică?",
        "choices": ["PyQt", "Tkinter", "React", "Swing"],
        "answer": "Tkinter"
    },
    {
        "question": "Care este simbolul pentru atribuirea unei valori?",
        "choices": ["=", "==", ":=", "::"],
        "answer": "="
    },
    {
        "question": "Care este indexul primului element dintr-o listă?",
        "choices": ["0", "1", "-1", "None"],
        "answer": "0"
    }
]
#Am creat clasa care defineste codul trivia
class TriviaGame:
    def __init__(self, root):
        self.root = root #este fereastra principala
        self.root.title("Joc Trivia")  #titlul ferestrei
        self.current = 0 #indexul de intrebari curente
        self.score = 0 #scorul acumulat
        
        #Eticheta unde se va afisa intrebarea
        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20) #spatiu de sus-jos

        #Frame in care se adauga butoanele pentru variantele de raspuns
        self.buttons_frame = tk.Frame(root) #un frame organizeaza elementele pe sectiuni, evita aglomerarea directa in fereastra principala
        self.buttons_frame.pack()

        #Adaugam eticheta unde se afiseaza daca ai raspuns corect sau gresit
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        #Incearca prima intrebare
        self.load_question()
        
    #Functie care incearca intrebarea curenta si creeaza butoane
    def load_question(self):
        self.result_label.config(text="") #goleste mesajul anterior
        #sterge butoanele vechi, daca exista
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        
        q = questions[self.current] #obtine intrebarea curenta
        self.question_label.config(text=q["question"]) #afiseaza intrebarea

        #Se creeaza cate un buton p[entru fiecare varianta 
        for choice in q["choices"]:
            btn = tk.Button(self.buttons_frame, text=choice, font=("Arial", 12), width=20,
                            command=lambda c=choice: self.check_answer(c)) #cand se apasa, trimite raspunsul
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
