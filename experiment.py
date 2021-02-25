import os
import random
from datetime import datetime
from time import sleep
import tkinter as tk
from tkinter import messagebox



MIN = 1000
MAX = 7000
FNAME = r"{}".format(os.path.join(os.path.dirname(os.path.realpath(__file__)), "results.txt".replace("\\\\", "\\")))



class Experiment():

    def __init__(self, number_of_experiments):
        self.data    = []
        self.timer   = None
        self.started = False
        self.exptype = "one"
        self.maxexp  = number_of_experiments
        self.currexp = 1
        self.init()


    def init(self):
        self.root = tk.Tk(className=" Donder's Experiment")
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.bind("<space>", self.next)
        self.root.bind("<Left>", self.next)
        self.root.bind("<Right>", self.next)
        self.root.configure(bg="black")

        # Store list of circle configuration
        self.lcircle = [w//4, h//2, 150, "gray5"]
        self.mcircle = [w//2, h//2, 150, "gray5"]
        self.rcircle = [w*3//4, h//2, 150, "gray5"]

        # Create canvas with three circles
        self.canvas = tk.Canvas(self.root, bg="black")
        self.circle(self.lcircle, self.canvas)
        self.circle(self.mcircle, self.canvas)
        self.circle(self.rcircle, self.canvas)
        self.canvas.pack(fill="both", expand=True)

        # Start Button
        start = tk.Button(self.root, text="Start", bg="grey", fg="white", height=2, width=20)
        start.bind("<Button-1>", self.run)
        start.pack(side="bottom", pady=50)

        self.root.mainloop()


    def run(self, event):
        print("Starting experiment 1... <center flash>")
        messagebox.showinfo("Exp 1 - {} Iterations".format(self.maxexp), "Press <SPACE> when you see white!")
        self.started = True
        self.canvas.after(random.randint(MIN,MAX), self.iteration)


    def iteration(self):
        if self.exptype == "one":
            self.mcircle[-1] = "white"
            self.timer = datetime.now()
            self.circle(self.mcircle, self.canvas)
        else:
            self.timer = datetime.now()
            c = self.lcircle if random.random() < 0.5 else self.rcircle
            c[-1] = "white"
            self.circle(c, self.canvas)


    def next(self, event):

        # Deal with game not started / wrong key pressed cases
        k = event.keysym
        print("Started: [{}] Key: [{}] Iteration: [{}]".format(self.started, k, self.currexp))
        if self.started == False:
            return
        if self.lcircle[-1] == "white" and k != "Left" or self.mcircle[-1] == "white" and k != "space" or self.rcircle[-1] == "white" and k != "Right":
            print("user pressed wrong key... skipping")
            self.clear()
            self.canvas.after(random.randint(MIN,MAX), self.iteration)
            return 

        # Record data and proceed with next experiment iteration
        diff = datetime.now() - self.timer
        self.data.append((k, diff.total_seconds()*1000, self.exptype))
        if self.currexp == self.maxexp and self.exptype == "one":
            messagebox.showinfo("Exp 2 - {} Iterations".format(self.maxexp), "Press <LEFTARROW> when you see a white circle on the left and <RIGHTARROW> when you see a white circle on the right!")
            self.currexp = 0
            self.exptype = "two"
            self.iteration()
        elif self.currexp == self.maxexp and self.exptype == "two":
            print("experiment concluding, writing text file and exiting")
            self.results()
            self.root.quit()
        elif self.exptype == "one":
            self.iteration()
        elif self.exptype == "two":
            self.iteration()
        else:
            print("!!! FATAL ERROR !!!")
            sys.exit(0)

        self.currexp += 1
        self.clear()
        self.canvas.after(random.randint(MIN,MAX), self.iteration)


    def clear(self):
        self.lcircle[-1] = "gray5"
        self.mcircle[-1] = "gray5"
        self.rcircle[-1] = "gray5"
        self.circle(self.lcircle, self.canvas)
        self.circle(self.mcircle, self.canvas)
        self.circle(self.rcircle, self.canvas)


    def results(self):
        messagebox.showinfo("Finished", "Press <OK> to generate results!")
        l = len(self.data)
        try:
            with open(FNAME, "w") as fout:
                total = 0
                fout.write("CENTER LIGHT\n")
                for i in range(0, l//2):
                    fout.write("{}\n".format(self.data[i][1]))
                    total += self.data[i][1]
                fout.write("AVERAGE: {}\n".format(total / (l//2)))
                fout.write("\n===============================\n\n")
                total = 0
                fout.write("LEFT OR RIGHT LIGHT\n")
                for i in range(l//2, l):
                    fout.write("{}\n".format(self.data[i][1]))
                    total += self.data[i][1]
                fout.write("AVERAGE: {}\n".format(total / (l//2)))
            print("results written to {}".format(FNAME))
        except Exception as e:
            print("ERROR: could not write results [{}]".format(e))


    def circle(self, c, canvas):
        x, y, r, fill =  c[0], c[1], c[2], c[3]
        return self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=fill)



if __name__ == "__main__":
    e = Experiment(10)