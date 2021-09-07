from tkinter import *
# from buttons import Buttonsaction, Operations_main
import buttons as b


class Calc_app(Tk):

    def __init__(self):

        Tk.__init__(self)
        
        self.title('Calc')
        self.geometry('+900+300')
        self.resizable(False, False)
        # self.iconbitmap('calc_calculator_2183.ico')
        self.set_ui()


    def set_ui(self):

        self.entry = Entry(self, font=('Segoe UI', 12, 'bold'), text=0, width='30', justify=RIGHT)
        self.entry.insert(0, '0')
        self.entry.grid(row=0, column=0, columnspan=4)

        Buttons = b.Buttonsaction()



        btn_del = Button(font=('Segoe UI', 14, 'bold'), text='Del', width=6, bg='#DCDCDC', command=lambda: Buttons.btn_del_action(self)).grid(row=1, column=0)
        btn_square = Button(font=('Segoe UI', 14, 'bold'), text='x²', width=6, bg='#DCDCDC', command=lambda: Buttons.btn_square_action(self)).grid(row=1, column=1)
        btn_sqrt = Button(font=('Segoe UI', 14, 'bold'), text='²√x', width=6, bg='#DCDCDC', command=lambda: Buttons.btn_sqrt_action(self)).grid(row=1, column=2)
        btn_division = Button(font=('Segoe UI', 14, 'bold'), text='÷', width=4, bg='#DCDCDC', command=lambda: Buttons.btn_operation_action(self, 'division')).grid(row=1, column=3)

        btn_7 = Button(font=('Segoe UI', 14, 'bold'), text='7', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 7)).grid(row=2, column=0)
        btn_8 = Button(font=('Segoe UI', 14, 'bold'), text='8', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 8)).grid(row=2, column=1)
        btn_9 = Button(font=('Segoe UI', 14, 'bold'), text='9', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 9)).grid(row=2, column=2)
        btn_x = Button(font=('Segoe UI', 14, 'bold'), text='x', width=4, bg='#DCDCDC', command=lambda: Buttons.btn_operation_action(self, 'multiply')).grid(row=2, column=3)

        btn_4 = Button(font=('Segoe UI', 14, 'bold'), text='4', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 4)).grid(row=3, column=0)
        btn_5 = Button(font=('Segoe UI', 14, 'bold'), text='5', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 5)).grid(row=3, column=1)
        btn_6 = Button(font=('Segoe UI', 14, 'bold'), text='6', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 6)).grid(row=3, column=2)
        btn_minus = Button(font=('Segoe UI', 14, 'bold'), text='-', width=4, bg='#DCDCDC', command=lambda: Buttons.btn_operation_action(self, 'minus')).grid(row=3, column=3)

        btn_1 = Button(font=('Segoe UI', 14, 'bold'), text='1', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 1)).grid(row=4, column=0)
        btn_2 = Button(font=('Segoe UI', 14, 'bold'), text='2', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 2)).grid(row=4, column=1)
        btn_3 = Button(font=('Segoe UI', 14, 'bold'), text='3', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 3)).grid(row=4, column=2)
        btn_plus = Button(font=('Segoe UI', 14, 'bold'), text='+', width=4, bg='#DCDCDC', command=lambda: Buttons.btn_operation_action(self, 'plus')).grid(row=4, column=3)    
        
        btn_clear = Button(font=('Segoe UI', 14, 'bold'), text='C', width=6, bg='#DCDCDC', command=lambda: Buttons.btn_clear_action(self)).grid(row=5, column=0)
        btn_0 = Button(font=('Segoe UI', 14, 'bold'), text='0', width=6, bg='white', command=lambda: Buttons.btn_num_action(self, 0)).grid(row=5, column=1)
        btn_comma = Button(font=('Segoe UI', 14, 'bold'), text=',', width=6, bg='white', command=lambda: Buttons.btn_comma_action(self)).grid(row=5, column=2)
        btn_equal = Button(font=('Segoe UI', 14, 'bold'), text='=', width=4, bg='#DCDCDC', command=lambda: Buttons.btn_equal_action(self)).grid(row=5, column=3)

# https://stackoverflow.com/questions/2283210/python-function-pointer
if __name__ == '__main__':
    root = Calc_app()
    root.mainloop()
