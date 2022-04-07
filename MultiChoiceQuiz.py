"""Multi Choice Quiz with just one question"""

from multiprocessing.connection import answer_challenge
from tkinter import *

class MultiChoiceQuiz:

    def __init__(self, parent):
        self.answers = []
        self.q = Quiz()

        f1 = Frame(parent, bg = "#CFE2F3", height = 20, width = 300)
        f1.grid(column = 0, row = 0)
        f1.grid_propagate(0)

        f2 = Frame(parent, bg = "#CFE2F3", height = 300, width = 300)
        f2.grid(column = 0, row = 1)
        f2.grid_propagate(0)

        label1 = Label(f1, text = "Question: {}".format(self.q.question), bg = "#CFE2F3")
        label1.grid(column = 0, row = 0)

        label2 = Label(f2, text = "", bg = "#CFE2F3")
        label2.grid(column = 1, row = 0)

        self.v = StringVar()
        self.v.set("0")
        self.choices = []
        for i in range(len(self.q.choices)):
            self.choices.append(Radiobutton(f2, variable = self.v, value = self.q.choices[i], text = self.q.choices[i], bg = "#CFE2F3", command = self.configure_answer))
            self.choices[i].grid(row = i+1, sticky = W, padx = 50)

        self.label3 = Label(f2, text = "", bg = "#CFE2F3")
        self.label3.grid(column = 0, row = 5, sticky = W)

    def configure_answer(self):
        if self.q.check_answer(self.v.get()):
            self.label3.configure(text = "Correct!")
        else:
            self.label3.configure(text = "*Incorrect")


class Quiz:
    def __init__(self):
        self.question = "What is the capital of Mongolia?"
        self.choices = ["Vladivostok", "Astana", "Ulaanbaatar", "Lhasa"]

    def check_answer(self, answer):
        if answer == "Ulaanbaatar":
            return True
        return False



#Main Routine
if __name__ == "__main__":
    root = Tk()
    mcq = MultiChoiceQuiz(root)
    root.title("Multi Choice Quiz")

    root.mainloop()


