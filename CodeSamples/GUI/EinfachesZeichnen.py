import tkinter as tk

class EinfachesZeichnen:
    def __init__(self, master):
        self.master = master
        
        # Canvas erstellen
        self.canvas = tk.Canvas(master, width=400, height=300, bg='white')
        self.canvas.pack(pady=20)
        
        # Koordinatensystem zeichnen
        self.zeichne_koordinatensystem()
        
        # Button zum Hinzufügen eines Punktes
        self.add_button = tk.Button(master, text="Punkt hinzufügen", 
                                  command=self.punkt_hinzufuegen)
        self.add_button.pack()
        
        # Entry-Felder für Koordinaten
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)
        
        tk.Label(self.frame, text="x:").pack(side=tk.LEFT)
        self.x_entry = tk.Entry(self.frame, width=5)
        self.x_entry.pack(side=tk.LEFT, padx=5)
        self.x_entry.insert(0, "1")
        
        tk.Label(self.frame, text="y:").pack(side=tk.LEFT)
        self.y_entry = tk.Entry(self.frame, width=5)
        self.y_entry.pack(side=tk.LEFT, padx=5)
        self.y_entry.insert(0, "1")
        
        # Koordinaten-Label
        self.coord_label = tk.Label(master, text="Noch keine Punkte")
        self.coord_label.pack()
        
        self.punkte = []
        
    def zeichne_koordinatensystem(self):
        # Hintergrundlinien
        for i in range(50, 350, 50):
            # Vertikale Linien
            self.canvas.create_line(i, 50, i, 250, fill='lightgray')
            # Horizontale Linien
            self.canvas.create_line(50, i, 350, i, fill='lightgray')
        
        # x-Achse
        self.canvas.create_line(50, 150, 350, 150, arrow=tk.LAST)
        # y-Achse
        self.canvas.create_line(200, 250, 200, 50, arrow=tk.LAST)
        
        # Beschriftung
        self.canvas.create_text(340, 170, text="x")
        self.canvas.create_text(180, 60, text="y")
        
        # Achsenbeschriftung
        for i in range(-3, 4):
            # x-Achse
            self.canvas.create_text(200 + i*50, 170, text=str(i))
            # y-Achse
            if i != 0:
                self.canvas.create_text(180, 150 - i*50, text=str(i))
        
    def punkt_hinzufuegen(self):
        try:
            # Koordinaten aus Entry-Feldern lesen
            x_wert = float(self.x_entry.get())
            y_wert = float(self.y_entry.get())
            
            # Umrechnung in Canvas-Koordinaten (50 Pixel = 1 Einheit)
            x = 200 + x_wert * 50
            y = 150 - y_wert * 50
            
            # Punkt nur zeichnen, wenn er im sichtbaren Bereich liegt
            if 50 <= x <= 350 and 50 <= y <= 250:
                punkt = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
                self.punkte.append((x_wert, y_wert))
                self.coord_label.config(text=f"Punkt bei ({x_wert}, {y_wert})")
            else:
                self.coord_label.config(text="Punkt außerhalb des sichtbaren Bereichs!")
        except ValueError:
            self.coord_label.config(text="Bitte gültige Zahlen eingeben!")

# Verwendung:
root = tk.Tk()
app = EinfachesZeichnen(root)
root.mainloop()