import tkinter as tk
import re


class Encoder:
    def __init__(self) -> None:
        self.gui = tk.Tk()
        self.gui.geometry("600x450")
        self.gui.title("HDB3")
        self.gui.configure(background="light gray")
        
        self.input = tk.StringVar()
       
        self.reg = re.compile("^[0-1]*$")

        self.uncorrert_input_label = tk.Label(text="Допустимый ввод - 0 и 1")
        self.uncorrert_input_label.configure(background="light gray")
        self.uncorrert_input_label.pack_forget()

        self.entry = tk.Entry(self.gui, textvariable=self.input, justify=tk.RIGHT)
        self.entry.pack()
        self.entry.place(x=50, y=0)

        self.canvas = tk.Canvas(self.gui, width=600, height=150)
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

    def hdb3(self, code_to_encode: str) -> list:
        zero_count, one_count = 0, 0        
        changed_by_hdb3 = []

        for i in code_to_encode:
            match i:
                case "0":
                    zero_count += 1
                case "1":
                    zero_count = 0
                    one_count += 1

            if zero_count == 4:
                match one_count % 2:
                    case 0:
                        changed_by_hdb3.append("v")
                        one_count += 1
                        
                    case _:
                        changed_by_hdb3[len(changed_by_hdb3)-3] = "(1)"
                        changed_by_hdb3.append("v")
                        one_count += 2

                zero_count = 0
                continue

            changed_by_hdb3.append(i)

        return changed_by_hdb3

    def draw(self, data: str):
        up = True
        x, y = 10, 50
        step_x, step_y = 20, 20

        changed_by_hdb3 = self.hdb3(self.input.get())

        for i in range(len(changed_by_hdb3)):
            item = changed_by_hdb3[i]
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
                
                case "(1)":
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

                case "v":
                    if not up:
                        self.canvas.create_line(x, y, x, y - step_y)
                        y -= step_y
                        self.canvas.create_line(x, y, x + step_x, y)
                        self.canvas.create_text(x + 10, 80, text=item)
                        x += step_x
                        self.canvas.create_line(x, y, x, y + step_y)
                        y += step_y
                    else:
                        self.canvas.create_line(x, y, x ,y + step_y)
                        y += step_y
                        self.canvas.create_line(x, y, x + step_x, y)
                        self.canvas.create_text(x + 10, 80, text=item)
                        x += step_x
                        self.canvas.create_line(x, y, x, y - step_y)
                        y -= step_y

    def run(self):
        self.gui.mainloop()


def main():
    encoder = Encoder()
    encoder.run()


if __name__ == "__main__":
    main()