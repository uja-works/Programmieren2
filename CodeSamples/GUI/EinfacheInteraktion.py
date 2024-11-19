import tkinter as tk

class EinfacheInteraktion:
    def __init__(self, master):
        self.master = master
        
        # Zähler für Klicks
        self.counter = 0
        
        # Label für Anzeigewert
        self.label = tk.Label(master, text="Wert: 0")
        self.label.pack(pady=20)
        
        # Buttons für +/- Operationen
        self.plus_button = tk.Button(master, text="+1", command=self.increment)
        self.plus_button.pack()
        
        self.minus_button = tk.Button(master, text="-1", command=self.decrement)
        self.minus_button.pack()
        
    def increment(self):
        self.counter += 1
        self.label.config(text=f"Wert: {self.counter}")
        
    def decrement(self):
        self.counter -= 1
        self.label.config(text=f"Wert: {self.counter}")

# Verwendung:
root = tk.Tk()
app = EinfacheInteraktion(root)
root.mainloop()