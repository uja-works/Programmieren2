import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
from numba import jit
from tkinter import Frame
from tkinter import TOP, BOTH, LEFT, NW

class MandelbrotApp:
    def __init__(self, root):
        self.root = root
        self.control_frame = Frame(root)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

        self.iteration_label = tk.Label(self.control_frame, text="Iterations:")
        self.iteration_label.pack(side=tk.LEFT)

        self.iterations = 256  # Define iterations before using it
        self.iteration_entry = tk.Entry(self.control_frame)
        self.iteration_entry.insert(0, str(self.iterations))
        self.iteration_entry.pack(side=tk.LEFT)

        self.update_button = tk.Button(self.control_frame, text="Update", command=self.update_iterations)
        self.update_button.pack(side=tk.LEFT)
        self.root.title("Mandelbrot Set Zoom")
        
        self.canvas = Canvas(root, width=800, height=800)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.image = Image.new("RGB", (800, 800))
        self.x_min, self.x_max = -2.0, 1.0
        self.y_min, self.y_max = -1.5, 1.5
        self.iterations = 256
        self.draw_mandelbrot()

        # Removed redundant widgets
        
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
       
        self.canvas.bind("<Button-1>", self.zoom_in)
        
    
    @staticmethod
    @jit(nopython=True)
    def mandelbrot_color(zx, zy, iterations):
        c = complex(zx, zy)
        z = 0.0j
        for i in range(iterations):
            z = z*z + c
            if (z.real*z.real + z.imag*z.imag) >= 4:
                ii = int((i/iterations)**0.2 * 255)
                #return (ii % 8 * 32, ii % 16 * 16, ii % 32 * 8)
                return (ii, ii*0,  0*ii//2)
        return (0, 0, 0)

    def update_iterations(self):
        try:
            self.iterations = int(self.iteration_entry.get())
            #self.draw_mandelbrot()
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
            self.draw_mandelbrot()
        except ValueError:
            print(ValueError)

    def draw_mandelbrot(self):
        print(f"Using {self.iterations} iterations.")
        for x in range(800):
            for y in range(800):
                zx, zy = self.pixel_to_complex(x, y)
                color = self.mandelbrot_color(zx, zy, self.iterations)
                self.image.putpixel((x, y), color)
    
    def pixel_to_complex(self, x, y):
        zx = x * (self.x_max - self.x_min) / 800 + self.x_min
        zy = y * (self.y_max - self.y_min) / 800 + self.y_min
        return zx, zy
    
    
    def zoom_in(self, event):
        x, y = event.x, event.y
        zx, zy = self.pixel_to_complex(x, y)
        
        zoom_factor = 0.5
        x_range = (self.x_max - self.x_min) * zoom_factor
        y_range = (self.y_max - self.y_min) * zoom_factor
        
        if event.state & 0x0001:  # Shift key is pressed
            zoom_factor = 2.0
        else:
            zoom_factor = 0.5

        x_range = (self.x_max - self.x_min) * zoom_factor
        y_range = (self.y_max - self.y_min) * zoom_factor

        self.x_min, self.x_max = zx - x_range / 2, zx + x_range / 2
        self.y_min, self.y_max = zy - y_range / 2, zy + y_range / 2
        self.y_min, self.y_max = zy - y_range / 2, zy + y_range / 2
        
        self.draw_mandelbrot()
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = MandelbrotApp(root)
    root.mainloop()