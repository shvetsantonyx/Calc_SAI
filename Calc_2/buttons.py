from tkinter.constants import END
from math import sqrt


class Buttonsaction:

    def __init__(self):

        self.marker_set = None
        self.marker_set_2 = False
        self.counter_operations = 0
        self.previous_res = 0
        self.previous_operation = None


    def btn_num_action(self, tkinter, constant):

        previous_num = tkinter.entry.get()

        if previous_num == '0':
            tkinter.entry.delete(first=0, last=END)
            tkinter.entry.insert(0, constant)
        elif previous_num == '0' and '.' in previous_num:
            tkinter.entry.insert(len(previous_num), constant)
        elif previous_num != '0' and '.' not in previous_num:
            tkinter.entry.insert(len(previous_num), constant)
        elif previous_num != 0 and '.' in previous_num:
            tkinter.entry.insert(len(previous_num), constant)

        
        if self.marker_set_2 == False:
            tkinter.entry.delete(first=0, last=END)
            self.marker_set_2 = True
            self.btn_num_action(tkinter, constant)

        self.previous_res = previous_num


    def btn_operation_action(self, tkinter, marker):

        if self.marker_set == None:
            self.previous_operation = marker
            self.marker_set = marker
            self.marker_set_2 = False
            self.counter_operations += 1

        else:  
            self.marker_set = marker
            self.marker_set_2 = False
            self.counter_operations += 1

        if self.counter_operations == 1:
            self.previous_marker = self.marker_set

        tkinter.previous_res = tkinter.entry.get()

        if self.marker_set == None:
            tkinter.entry.delete(first=0, last=END)
            tkinter.entry.insert(0, '0')

        if self.counter_operations > 1:
            tkinter.previous_res = self.previous_res
            self.equal_action(tkinter)
            tkinter.previous_res = tkinter.entry.get()
            

    def btn_square_action(self, tkinter):

        previous_num = float(tkinter.entry.get())
        tkinter.entry.delete(first=0, last=END)
        result = previous_num ** 2
        if str(result)[-1] == '0':
            tkinter.entry.insert(0, str(result)[:-2])
        else:
            tkinter.entry.insert(0, str(result))


    def btn_comma_action(self, tkinter):

        previous_num = tkinter.entry.get()

        if previous_num != 0 and '.' not in previous_num:
            tkinter.entry.insert(len(previous_num), '.')

        elif previous_num !=0 and '.' in previous_num:
            pass

        if previous_num == 0:
            tkinter.entry.insert(1, '.')


    def btn_del_action(self, tkinter):
        previous_num = tkinter.entry.get()

        if previous_num != '0':
            tkinter.entry.delete(first=(len(previous_num) - 1), last=None)


    def btn_sqrt_action(self, tkinter):

        previous_num = float(tkinter.entry.get())
        tkinter.entry.delete(first=0, last=END)
        result = sqrt(previous_num)
        if str(result)[-1] == '0':
            tkinter.entry.insert(0, str(result)[:-2])
        else:
            tkinter.entry.insert(0, str(result))

    def btn_clear_action(self, tkinter):

        tkinter.entry.delete(first=0, last=END)
        tkinter.entry.insert(0, '0')

        self.marker_set = None


    def btn_equal_action(self, tkinter):
         
        self.counter_operations = 0

        secondary_res = tkinter.entry.get()

        if self.marker_set == 'plus':
            result = round(float(tkinter.previous_res) + float(secondary_res), 10)
            tkinter.entry.delete(first=0, last=END)

            if str(result)[-1] == '0':
                tkinter.entry.insert(0, str(result)[:-2])
            else:
                tkinter.entry.insert(0, str(result))
                
        elif self.marker_set == 'minus':
            result = round(float(tkinter.previous_res) - float(secondary_res), 10)
            tkinter.entry.delete(first=0, last=END)
            if str(result)[-1] == '0':
                tkinter.entry.insert(0, str(result)[:-2])
            else:
                tkinter.entry.insert(0, str(result))

        elif self.marker_set == 'multiply':
            result = round(float(tkinter.previous_res) * float(secondary_res), 10)
            tkinter.entry.delete(first=0, last=END)
            if str(result)[-1] == '0':
                tkinter.entry.insert(0, str(result)[:-2])
            else:
                tkinter.entry.insert(0, str(result))

        elif self.marker_set == 'division':
            try:
                tkinter.entry.delete(first=0, last=END)
                result = round(float(tkinter.previous_res) / float(secondary_res), 10)

                if str(result)[-1] == '0':
                    tkinter.entry.insert(0, str(result)[:-2])
                else:
                    tkinter.entry.insert(0, str(result))
            except ZeroDivisionError:
                tkinter.entry.insert(0, '∞')

        else:
            try:
                pass
            except: NameError


    def equal_action(self, tkinter):
        
        secondary_res = tkinter.entry.get()

        if self.previous_operation == 'plus':
            result = round(float(tkinter.previous_res) + float(secondary_res), 10)
            tkinter.entry.delete(first=0, last=END)

            if str(result)[-1] == '0':
                tkinter.entry.insert(0, str(result)[:-2])
            else:
                tkinter.entry.insert(0, str(result))
                
        elif self.previous_operation == 'minus':
            result = round(float(tkinter.previous_res) - float(secondary_res), 10)
            tkinter.entry.delete(first=0, last=END)
            if str(result)[-1] == '0':
                tkinter.entry.insert(0, str(result)[:-2])
            else:
                tkinter.entry.insert(0, str(result))

        elif self.previous_operation == 'multiply':
            result = round(float(tkinter.previous_res) * float(secondary_res), 10)
            tkinter.entry.delete(first=0, last=END)
            if str(result)[-1] == '0':
                tkinter.entry.insert(0, str(result)[:-2])
            else:
                tkinter.entry.insert(0, str(result))

        elif self.previous_operation == 'division':
            try:
                tkinter.entry.delete(first=0, last=END)
                result = round(float(tkinter.previous_res) / float(secondary_res), 10)

                if str(result)[-1] == '0':
                    tkinter.entry.insert(0, str(result)[:-2])
                else:
                    tkinter.entry.insert(0, str(result))
            except ZeroDivisionError:
                tkinter.entry.insert(0, '∞')

        else:
            try:
                pass
            except: NameError
