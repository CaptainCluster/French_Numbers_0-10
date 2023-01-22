#Made by CaptainCluster
from tkinter import *
import random

class PROGRAM():
    def __init__(self):
        self.Corrects = 0
        self.Wrongs = 0
        self.Sample = ""

        Root = Tk()
        Root.title("French numbers 0-10")
        Root.configure(width=370, height=200, bg="black")
        Root.resizable(0,0)
        Root.pack_propagate(0)

        MainFrame = Frame(Root, width=340, height=200, bg = "blue")
        MainFrame.pack(pady = 15)
        MainFrame.grid_propagate(0)

        Label(MainFrame, text = "The number", width = 15).grid(column = 0, row = 0, pady = 5)
        self.Number = Entry(MainFrame, width = 10, justify = "center")
        self.Number.grid(column = 1, row = 0)

        Label(MainFrame, text = "Your translation", width = 15).grid(column = 0, row = 1, padx = 5)
        self.Translation = Entry(MainFrame, width = 10, justify = "center")
        self.Translation.grid(column = 1, row = 1)

        Label(MainFrame, text = "Correct").grid(column = 2, row = 0)
        Label(MainFrame, text = "Wrong").grid(column = 3, row = 0)
        
        self.Correct = Entry(MainFrame, width = 10, justify = "center")
        self.Correct.grid(column = 2, row = 1, padx = 5)
        self.Wrong = Entry(MainFrame, width = 10, justify = "center")
        self.Wrong.grid(column = 3, row = 1, padx = 5)
        
        self.Correct.insert(0, self.Corrects)
        self.Wrong.insert(0,self.Wrongs)

        self.Answer = self.newQuestion()
        self.Number.configure(state = "disabled")
        self.Correct.configure(state = "disabled")
        self.Wrong.configure(state = "disabled")

        Button(MainFrame, text = "Press to translate", command = self.process).grid(column = 0, row = 2, pady = 5)
        Button(MainFrame, text = "Instructions", width = 13, command = self.instructions).grid(column = 0, row = 3)

        self.Frame = Frame(MainFrame, width = 210, height = 90, bg = "white")
        self.Frame.place(x = 120, y = 70)
        self.Frame.pack_propagate(0)
        Root.mainloop()
        return None

    def randomizer(self): #Selects a random number that determines what number will be asked
        Sample = random.sample(range(0,11), 1)
        Sample = Sample[0]
        Sample = self.verifyNumber(Sample)
        return Sample

    def verifyNumber(self, Sample):
        if(Sample == self.Sample):
            Sample = self.randomizer()
            Sample = self.verifyNumber(Sample)
        return Sample


    def gatherInfo(self, Sample): #Matches the number sample with a matching French translation (in letters)
        Numbers = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix"]
        for i in range(0,11):
            if(Sample == i):
                Answer = Numbers[i]
                break
        return Answer

    def inspect(self, UserAnswer): #Checks whether the user has answered correctly or not
        if(self.Answer == UserAnswer):
            self.Corrects = self.Corrects + 1
            self.notification("Your answer is correct!", "green")
        elif(UserAnswer == ""):
            self.notification("Please answer the question!", "red")
        else:
            self.Wrongs = self.Wrongs + 1
            self.notification("Your answer is wrong!", "red")
        self.updateResults()
        return None

    def updateResults(self):
        self.Correct.configure(state = "normal")
        self.Correct.delete(0, END)
        self.Correct.insert(0, self.Corrects)
        self.Correct.configure(state = "disabled")
        self.Wrong.configure(state = "normal")
        self.Wrong.delete(0, END)
        self.Wrong.insert(0, self.Wrongs)
        self.Wrong.configure(state = "disabled")
        return None

    def newQuestion(self):
        self.Number.configure(state = "normal")
        Sample = self.randomizer()
        Answer = self.gatherInfo(Sample)
        self.Number.delete(0, END)
        self.Number.insert(0, Sample)
        self.Number.configure(state = "disabled")
        return Answer

    def process(self):
        self.Number.configure(state = "normal")
        UserAnswer = self.Translation.get()
        self.inspect(UserAnswer)
        if(UserAnswer != ""):
            Sample = self.randomizer()
            self.Answer = self.gatherInfo(Sample)
            self.Sample = Sample
            self.Number.delete(0, END)
            self.Number.insert(0, Sample)
        self.Number.configure(state = "disabled")
        return None

    def notification(self, Written, Color):
        self.Notifications = Label(self.Frame, text = Written, fg = Color, bg = "white")
        self.Notifications.pack()
        self.Notifications.after(2000, self.Notifications.destroy)
        return None

    def instructions(self):
        newroot = Tk()
        newroot.title("Instructions")
        newroot.configure(bg = "white")
        newroot.resizable(0,0)
        Label(newroot, text = "Greetings. This program is designed to help you learn").grid()
        Label(newroot, text = "how to translate the numbers ranging from 0-10.").grid()
        Label(newroot, text = "to French. The program calculates how many times").grid()
        Label(newroot, text = "you have been successful at translating and how").grid()
        Label(newroot, text = "many times you have failed at doing so.").grid()
        newroot.mainloop()
        return None

PROGRAM()


