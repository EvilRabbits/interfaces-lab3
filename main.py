import tkinter as tk


class Encoder:
    def __init__(self) -> None:
        self.gui = tk.Tk()
        self.gui.geometry("600x150")
        self.gui.title("HDB3")
        self.gui.configure(background="light gray")

        self.name = tk.StringVar()
        self.label = tk.Label(text="Введите 0 и 1")
        self.label.pack_forget()

        self.entry = tk.Entry(self.gui, textvariable=self.name, justify=tk.RIGHT)
        self.entry.pack()
        self.entry.place(x=50, y=0)

        self.canvas = tk.Canvas(self.gui, width=600, height=150)
        self.canvas.pack()
        self.canvas.place(x=0, y=50)

        self.button = tk.Button(self.gui, text = "Обработать")
        self.button.configure(background="light gray", width=9)
        self.button.pack()
        self.button.place(x=50, y=22)
        self.button.bind("<Button-1>", self.draw)        


    def draw(self, event):
        zero_count, one_count = 0, 0
        up = True
        x, y = 10, 50
        step_x, step_y = 20, 20
        
        self.canvas.delete("all")
    
    def run(self):
        self.gui.mainloop()


def main():
    encoder = Encoder()
    encoder.run()


if __name__ == "__main__":
    main()