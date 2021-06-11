import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):

        window = Tk()
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window, text='샌드위치(5000원)').grid(column = 0, row = 0)
        Label(window, text='케이크(20000원)').grid(column = 0, row = 1)

        num1 = Entry(window, width = 10)
        num2 = Entry(window, width = 10)

        num1.grid(column = 1, row = 0)
        num2.grid(column = 1, row = 1)

        btn_plus = Button(window, text = "주문하기", command=lambda:self.send_order(num1.get(), num2.get()))
        btn_plus.grid(column=0, row=2)

    def send_order(self, num1, num2):
        try:
            num1 = int(num1)
            num2 = int(num2)

            if num1 < 0 and num2 < 0:
                return
            else:
                if num1 == 0: #샌드위치가 0개인 경우
                    text = ("{}: 케이크 (20000원) {}개".format(self.name, num2))
                    self.bakeryView.add_order(text)
                elif num2 == 0: #케이크가 0개인 경우
                    text = (self.name, ": 샌드위치(5000원)", num1)
                    text = ("{}: 샌드위치 (5000원) {}개".format(self.name, num1))
                    self.bakeryView.add_order(text)
                else:
                    text = ("{}: 샌드위치 (5000원) {}개, 케이크 (20000원) {}개".format(self.name, num1, num2))
                    self.bakeryView.add_order(text)

        except:
            return


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
