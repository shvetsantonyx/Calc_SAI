from tkinter.constants import END
from math import sqrt


class Buttonsaction:

    # marker for operations: plus, minus, multyply, division
    global marker_set
    marker_set = None

    # marker for new turn of btn_num_action after operations
    global marker_set_2
    marker_set_2 = True


    def btn_num_action(self, constant):

        BTN = constant

        previous_num = self.entry.get()


        if previous_num == '0':
            self.entry.delete(first=0, last=END)
            self.entry.insert(0, BTN)
        elif previous_num == '0' and '.' in previous_num:
            self.entry.insert(len(previous_num), BTN)
        elif previous_num != '0' and '.' not in previous_num:
            self.entry.insert(len(previous_num), BTN)
        elif previous_num != 0 and '.' in previous_num:
            self.entry.insert(len(previous_num), BTN)

        
        global marker_set_2
        if marker_set_2 == False:
            self.entry.delete(first=0, last=END)
            marker_set_2 = True
            self.btn_num_action(constant)


    def btn_operation_action(self, marker):

        global marker_set
        marker_set = marker

        global marker_set_2
        marker_set_2 = False

        global previous_res
        previous_res = self.entry.get()

        if marker_set == None:
            self.entry.delete(first=0, last=END)
            self.entry.insert(0, '0')


    def btn_square_action(self):

        previous_num = float(self.entry.get())
        self.entry.delete(first=0, last=END)
        result = previous_num ** 2
        if str(result)[-1] == '0':
            self.entry.insert(0, str(result)[:-2])
        else:
            self.entry.insert(0, str(result))


    def btn_comma_action(self):

        previous_num = self.entry.get()

        if previous_num != 0 and '.' not in previous_num:
            self.entry.insert(len(previous_num), '.')

        elif previous_num !=0 and '.' in previous_num:
            pass

        if previous_num == 0:
            self.entry.insert(1, '.')


    def btn_del_action(self):
        previous_num = self.entry.get()

        if previous_num != '0':
            self.entry.delete(first=(len(previous_num) - 1), last=None)

    def btn_sqrt_action(self):

        previous_num = float(self.entry.get())
        self.entry.delete(first=0, last=END)
        result = sqrt(previous_num)
        if str(result)[-1] == '0':
            self.entry.insert(0, str(result)[:-2])
        else:
            self.entry.insert(0, str(result))

    def btn_clear_action(self):

        self.entry.delete(first=0, last=END)
        self.entry.insert(0, '0')

        global marker_set
        marker_set = None

    def btn_equal_action(self):
        print(marker_set)
        print(previous_res)
        

        secondary_res = self.entry.get()
        print(secondary_res)

        if marker_set == 'plus':
            result = round(float(previous_res) + float(secondary_res), 10)
            self.entry.delete(first=0, last=END)

            if str(result)[-1] == '0':
                self.entry.insert(0, str(result)[:-2])
            else:
                self.entry.insert(0, str(result))
                
        elif marker_set == 'minus':
            result = round(float(previous_res) - float(secondary_res), 10)
            self.entry.delete(first=0, last=END)
            if str(result)[-1] == '0':
                self.entry.insert(0, str(result)[:-2])
            else:
                self.entry.insert(0, str(result))

        elif marker_set == 'multiply':
            result = round(float(previous_res) * float(secondary_res), 10)
            self.entry.delete(first=0, last=END)
            if str(result)[-1] == '0':
                self.entry.insert(0, str(result)[:-2])
            else:
                self.entry.insert(0, str(result))

        elif marker_set == 'division':
            try:
                self.entry.delete(first=0, last=END)
                result = round(float(previous_res) / float(secondary_res), 10)

                if str(result)[-1] == '0':
                    self.entry.insert(0, str(result)[:-2])
                else:
                    self.entry.insert(0, str(result))
            except ZeroDivisionError:
                self.entry.insert(0, '∞')

        else:
            try:
                pass
            except: NameError

# class B(Buttonsaction):
#     def func(self):
#         if marker_set != None:
#             Buttonsaction.btn_equal_action()
