from tkinter import *
from tkmacosx import Button
from calculator_brain import CalculatorBrain

BUTTON_FONT = ("Arial", 20, "normal")
ANSWER_FONT = ("Arial", 50, "normal")


class CalculatorInterface:

    def __init__(self, calculator : CalculatorBrain):

        self.calculator = calculator

        self.root = Tk()
        self.root.title("Calculator")
        self.root.config(padx=5, pady=5)

        self.screen_label = Label(text=self.calculator.answer, anchor="e")
        self.screen_label.config(font=ANSWER_FONT)
        self.screen_label.grid(column=0, row=0, columnspan=4)

        self.clear_button = Button(text="CLEAR", height=50, width=150, font=BUTTON_FONT, command=self.pressed_clear)
        self.clear_button.grid(column=0, row=1, columnspan=3)

        self.button0 = Button(text="0", height=50, width=150, font=BUTTON_FONT, command=self.pressed_0)
        self.button0.grid(column=0, row=5, columnspan=3)

        self.button1 = Button(text="1", height=50, width=50, font=BUTTON_FONT, command=self.pressed_1)
        self.button1.grid(column=0, row=4)

        self.button2 = Button(text="2", height=50, width=50, font=BUTTON_FONT, command=self.pressed_2)
        self.button2.grid(column=1, row=4)

        self.button3 = Button(text="3", height=50, width=50, font=BUTTON_FONT, command=self.pressed_3)
        self.button3.grid(column=2, row=4)

        self.button4 = Button(text="4", height=50, width=50, font=BUTTON_FONT, command=self.pressed_4)
        self.button4.grid(column=0, row=3)

        self.button5 = Button(text="5", height=50, width=50, font=BUTTON_FONT, command=self.pressed_5)
        self.button5.grid(column=1, row=3)

        self.button6 = Button(text="6", height=50, width=50, font=BUTTON_FONT, command=self.pressed_6)
        self.button6.grid(column=2, row=3)

        self.button7 = Button(text="7", height=50, width=50, font=BUTTON_FONT, command=self.pressed_7)
        self.button7.grid(column=0, row=2)

        self.button8 = Button(text="8", height=50, width=50, font=BUTTON_FONT, command=self.pressed_8)
        self.button8.grid(column=1, row=2)

        self.button9 = Button(text="9", height=50, width=50, font=BUTTON_FONT, command=self.pressed_9)
        self.button9.grid(column=2, row=2)

        self.equals_button = Button(text="=", height=50, width=50, font=BUTTON_FONT, command=self.pressed_equals)
        self.equals_button.grid(column=3, row=5)

        self.add_button = Button(text="+", height=50, width=50, font=BUTTON_FONT, command=self.pressed_add)
        self.add_button.grid(column=3, row=4)

        self.subtract_button = Button(text="-", height=50, width=50, font=BUTTON_FONT, command=self.pressed_subtract)
        self.subtract_button.grid(column=3, row=3)

        self.multiply_button = Button(text="x", height=50, width=50, font=BUTTON_FONT, command=self.pressed_multiply)
        self.multiply_button.grid(column=3, row=2)

        self.divide_button = Button(text="/", height=50, width=50, font=BUTTON_FONT, command=self.pressed_divide)
        self.divide_button.grid(column=3, row=1)

        self.num_input = ""

        self.num_being_inputted = 1

        self.nums = []

        self.root.mainloop()

    def update_screen(self):
        if self.num_input != "":
            self.screen_label.config(text=self.num_input)
        else:
            self.screen_label.config(text="0")

    def pressed_0(self):
        if self.num_input != "":
            self.num_input += "0"
            self.update_screen()

    def pressed_1(self):
        self.num_input += "1"
        self.update_screen()

    def pressed_2(self):
        self.num_input += "2"
        self.update_screen()

    def pressed_3(self):
        self.num_input += "3"
        self.update_screen()

    def pressed_4(self):
        self.num_input += "4"
        self.update_screen()

    def pressed_5(self):
        self.num_input += "5"
        self.update_screen()

    def pressed_6(self):
        self.num_input += "6"
        self.update_screen()

    def pressed_7(self):
        self.num_input += "7"
        self.update_screen()

    def pressed_8(self):
        self.num_input += "8"
        self.update_screen()

    def pressed_9(self):
        self.num_input += "9"
        self.update_screen()

    def pressed_clear(self):
        self.num_input = ""
        self.update_screen()

    def update_nums(self):
        if self.num_being_inputted == 1:
            self.calculator.num1 = float(self.num_input)
            self.num_being_inputted = 2
        else:
            self.calculator.num2 = float(self.num_input)
            self.num_being_inputted = 1
        self.nums.append(self.num_input)
        self.num_input = ""
        self.update_screen()

    def pressed_add(self):
        if self.num_input != "":
            self.calculator.operation = "+"
            self.update_nums()

    def pressed_subtract(self):
        if self.num_input != "":
            self.calculator.operation = "-"
            self.update_nums()

    def pressed_multiply(self):
        if self.num_input != "":
            self.calculator.operation = "*"
            self.update_nums()

    def pressed_divide(self):
        if self.num_input != "":
            self.calculator.operation = "/"
            self.update_nums()

    def pressed_equals(self):
        if self.num_input != "":
            self.update_nums()
            self.calculator.perform_calculation()
            self.num_input = f"{self.calculator.answer}"
            self.num_being_inputted = 1
            self.update_screen()

