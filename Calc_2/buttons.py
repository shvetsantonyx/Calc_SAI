from tkinter.constants import END
from math import sqrt


class Buttonsaction:

    # marker for operations: plus, minus, multyply, division
    # global marker_set
    # marker_set = None

    # # marker for new turn of btn_num_action after operations
    # global marker_set_2
    # marker_set_2 = True


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

        
        if self.marker_set_2 == False:
            self.entry.delete(first=0, last=END)
            self.marker_set_2 = True
            self.btn_num_action(constant)

        


class Operations_main(Buttonsaction):

    def btn_operation_action(self, marker):

        # global marker_set
        self.marker_set = marker

        # global marker_set_2
        self.marker_set_2 = False

        # global previous_res
        self.previous_res = self.entry.get()

        if self.marker_set == None:
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

        self.marker_set = None


class Equal_action(Operations_main):
    def btn_equal_action(self):
        # print(marker_set)
        # print(self.previous_res)
        

        secondary_res = self.entry.get()
        print(secondary_res)

        if self.marker_set == 'plus':
            result = round(float(self.previous_res) + float(secondary_res), 10)
            self.entry.delete(first=0, last=END)

            if str(result)[-1] == '0':
                self.entry.insert(0, str(result)[:-2])
            else:
                self.entry.insert(0, str(result))
                
        elif self.marker_set == 'minus':
            result = round(float(self.previous_res) - float(secondary_res), 10)
            self.entry.delete(first=0, last=END)
            if str(result)[-1] == '0':
                self.entry.insert(0, str(result)[:-2])
            else:
                self.entry.insert(0, str(result))

        elif self.marker_set == 'multiply':
            result = round(float(self.previous_res) * float(secondary_res), 10)
            self.entry.delete(first=0, last=END)
            if str(result)[-1] == '0':
                self.entry.insert(0, str(result)[:-2])
            else:
                self.entry.insert(0, str(result))

        elif self.marker_set == 'division':
            try:
                self.entry.delete(first=0, last=END)
                result = round(float(self.previous_res) / float(secondary_res), 10)

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
