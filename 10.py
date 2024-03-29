from tkinter import *


class OrderUp(Frame):
    def __init__(self, master):
        super(OrderUp, self).__init__(master)
        self.grid()  # Use grid for app
        self.create_welcome()
        self.create_starters()
        self.create_main_course()
        self.create_desert()
        self.create_submit()

    def create_welcome(self):
        Label(self, text="OrderUP App!\n\nPlease choose one of each and submit!", fg='red')\
            .grid(row=0, column=0, columnspan=2, sticky=W)

    def create_starters(self):
        self.start_dish = StringVar()
        self.start_dish.set(None)
        Label(self, text='\n\t--- STARTERS ---\n').grid(row=1, column=0, sticky=W)
        starter = ["French fries", "Salad", "Chilli Mushroom"]
        row = 2
        for dish in starter:
            Radiobutton(self, text=dish, variable=self.start_dish, value=dish).grid(row=row, column=0, sticky=W)
            row += 1

    def create_main_course(self):
        self.main_dish = StringVar()
        self.main_dish.set(None)
        Label(self, text='\n\t--- MAIN COURSE ---\n').grid(row=5, column=0, sticky=W)
        main = ["Tacos", "Fried Rice"]
        row = 6
        for dish in main:
            Radiobutton(self, text=dish, variable=self.main_dish, value=dish).grid(row=row, column=0, sticky=W)
            row += 1

    def create_desert(self):
        self.desert_dish = StringVar()
        self.desert_dish.set(None)
        Label(self, text='\n\t--- DESERT ---\n').grid(row=8, column=0, sticky=W)
        desert = ["Ice cream", "Jilebi"]
        row = 9
        for dish in desert:
            Radiobutton(self, text=dish, variable=self.desert_dish, value=dish).grid(row=row, column=0, sticky=W)
            row += 1

    def create_submit(self):
        Label(self).grid(row=11)  # Empty label
        Button(self, text="Order Food!", command=self.calculate_price).grid(row=12, column=0)

    def create_price_field(self, text):
        self.price_field = Label(self, text=text).grid(row=13, column=0)

    def calculate_price(self):
        self.total_price = 0
        starter = self.start_dish.get()
        main_course = self.main_dish.get()
        desert = self.desert_dish.get()
        food_price = [["French fries", 10],
                         ["Salad", 5],
                         ["Chilli Mushroom", 12],
                         ["Tacos", 20],
                         ["Fried Rice", 25],
                         ["Ice cream", 5],
                         ["Jilebi", 9]]
        for food, price in food_price:
            if starter in food:
                self.total_price += price
            if main_course in food:
                self.total_price += price
            if desert in food:
                self.total_price += price
        self.update_order(starter, main_course, desert)

    def update_order(self, starter, main_course, desert):
        text = ""
        text += "\nOrdered: \n\n{0}\n{1}\n{2}".format(starter, main_course, desert)
        text += "\n\nTotal price is: {0}".format(self.total_price)

        self.create_price_field(text)
