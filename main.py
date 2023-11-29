import tkinter as tk

class mycalculator:
    def __init__(self):
        
        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title('my calculator')

        self.label = tk.Label(self.root, text='my calculator', font=('Arial', 18))
        self.label.pack()

        self.button=tk.Button(self.root, text='c', height=3, width=10)
        self.button.place(x=0, y=35)

        self.button=tk.Button(self.root, text='7', height=3, width=10)
        self.button.place(x=0, y=85)

        self.button=tk.Button(self.root, text='4', height=3, width=10)
        self.button.place(x=0, y=135)

        self.button=tk.Button(self.root, text='1', height=3, width=10)
        self.button.place(x=0, y=185)

        self.button=tk.Button(self.root, text='0', height=3, width=20)
        self.button.place(x=0, y=235)

        self.button=tk.Button(self.root, text='+/-', height=3, width=10)
        self.button.place(x=80, y=35)
        

        self.root.mainloop()

mycalculator()