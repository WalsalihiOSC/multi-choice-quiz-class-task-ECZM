"""Multi Choice Quiz with just one question"""

from tkinter import *

class MultiChoiceQuiz:

    def __init__(self, parent):
        f1 = Frame(parent, bg = "#CFE2F3", height = 300, width = 300)
        f1.grid(column = 0, row = 0)

        f1.grid_propagate(0)

        label1 = Label(f1, text = "Question:", bg = "#CFE2F3")
        label1.grid(column = 0, row = 0)

        label2 = Label(f1, text = "What is the capital of Mongolia?", bg = "#CFE2F3")
        label2.grid(column = 1, row = 0)

        self.v = StringVar()
        self.v.set("0")
        choice = ["Vladivostok", "Astana", "Ulaanbaatar", "Lhasa"]
        self.choices = []
        for i in range(len(choice)):
            self.choices.append(Radiobutton(f1, variable = self.v, value = choice[i], text = choice[i], bg = "#CFE2F3", command = self.answer))
            self.choices[i].grid(column = 1, row = i+1, sticky = W, padx = 20)

        self.label3 = Label(f1, text = "", bg = "#CFE2F3")
        self.label3.grid(column = 0, row = 5)

    def answer(self):
        if self.v.get() == "Ulaanbaatar":
            self.label3.configure(text = "Correct!")
        else:
            self.label3.configure(text = "Incorrect")





#Main Routine
if __name__ == "__main__":
    root = Tk()
    mcq = MultiChoiceQuiz(root)
    root.title("Multi Choice Quiz")
    root.mainloop()


