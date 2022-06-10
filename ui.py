from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_text = Label(text="Score: 0", font=('arial', 15), bg=THEME_COLOR, fg='white')
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas_text = self.canvas.create_text(150,
                                                   125,
                                                   width=280,
                                                   text="Some Question Text",
                                                   font=('arial', 20, 'italic')
                                                   )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_image,
                                  bg=THEME_COLOR,
                                  highlightthickness=0,
                                  bd=1,
                                  command=self.true_button
                                  )
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image,
                                   bg=THEME_COLOR,
                                   highlightthickness=0,
                                   bd=1,
                                   command=self.false_button
                                   )
        self.false_button.grid(row=2, column=1)
        self.get_next_question_text()

        self.window.mainloop()

    def get_next_question_text(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.canvas_text, text="You reached end of quiz.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_button(self):
        self.feed_back(self.quiz.check_answer('True'))

    def false_button(self):
        self.feed_back(self.quiz.check_answer("False"))

    def feed_back(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_next_question_text)

