import tkinter as tk
import re


class Encoder:
    def __init__(self) -> None:
        self.gui = tk.Tk()
        self.gui.geometry("1000x450")
        self.gui.title("AMI")
        self.gui.configure(background="light gray")

        self.input = tk.StringVar()

        self.reg = re.compile("^[0-1]*$")

        self.uncorrert_input_label = tk.Label(text="Допустимый ввод - 0 и 1")
        self.uncorrert_input_label.configure(background="light gray")
        self.uncorrert_input_label.pack_forget()

        self.entry = tk.Entry(self.gui, textvariable=self.input, width=50, justify=tk.LEFT)
        self.entry.pack()
        self.entry.place(x=50, y=0)

        self.canvas = tk.Canvas(self.gui, width=1000, height=150)
        self.canvas.pack()
        self.canvas.place(x=0, y=50)

        self.handler_data_button = tk.Button(self.gui, text="Обработать")
        self.handler_data_button.configure(background="light gray", width=9)
        self.handler_data_button.pack()
        self.handler_data_button.place(x=50, y=22)
        self.handler_data_button.bind("<Button-1>", self.draw_one_event)

    def draw_one_event(self, event):
        self.canvas.delete("all")
        input_data = self.input.get()
        if self.reg.search(input_data) == None:
            self.uncorrert_input_label.pack()
            return 0

        self.draw(input_data)

    def draw(self, data: str):
        up = True
        x, y = 10, 50
        step_x, step_y = 20, 20

        for i in range(len(data)):
            item = data[i]
            match item:
                case "0":
                    self.canvas.create_line(x, y, x + step_x, y)
                    self.canvas.create_text(x + 10, 80, text=item)
                    x += step_x

                case "1":
                    if not up:
                        self.canvas.create_line(x, y, x, y + step_y)
                        y += step_y
                        self.canvas.create_line(x, y, x + step_x, y)
                        self.canvas.create_text(x + 10, 80, text=item)
                        x += step_x
                        self.canvas.create_line(x, y, x, y - step_y)
                        y -= step_y
                        up = True
                    else:
                        self.canvas.create_line(x, y, x ,y - step_y)
                        y -= step_y
                        self.canvas.create_line(x, y, x + step_x, y)
                        self.canvas.create_text(x + 10, 80, text=item)
                        x += step_x
                        self.canvas.create_line(x, y, x, y + step_y)
                        y += step_y
                        up = False

    def run(self):
        self.gui.mainloop()


def main():
    encoder = Encoder()
    encoder.run()


if __name__ == "__main__":
    main()
