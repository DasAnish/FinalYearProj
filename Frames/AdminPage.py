from tkinter import Scrollbar, Text, StringVar, VERTICAL, END
from tkinter.ttk import Frame, Label, Button, Entry, Combobox
from tkinter.messagebox import showinfo

LARGE_FONT = ('Comic Sans MS', 20)
MED_FONT = ('Comic Sans MS', 15)
SMALL_FONT = ('Comic Sans MS', 10)
ADMIN_PAGE, LOGIN_PAGE, RETAIL_PAGE, SIGN_UP_PAGE, VIEW_STOCK = [0, 1, 2, 3, 4]

class adminPage(Frame):
    def __init__(self, parent, main, **kw):
        Frame.__init__(self, parent, **kw)
        self.main = main
        self.label_head = Label(text='Admin Page', font = MED_FONT)
        self.adm_stock_l = Label(text='Stock Name: ')
        self.adm_stock = StringVar()
        self.adm_stock_c = Combobox(textvariable = self.adm_stock)
        self.adm_ncost_l = Label(text='New Cost of Stock: ')
        self.adm_namount_l = Label(text='New number of stocks added: ')
        self.adm_namount = Entry()
        self.adm_ncost = Entry()
        self.adm_update_b = Button(text='UPDATE', command = self.update)
        self.back_b = Button(text='Log Out', command = self.back)
        self.view_f_text = Text(height=20, width=30)
        self.view_scroll = Scrollbar(orient = VERTICAL, command=self.view_f_text.yview)
        self.view_f_text.config(yscrollcommand = self.view_scroll.set)
        self.new_stock = False
    def back(self):
        self.main.show_frame(LOGIN_PAGE, ADMIN_PAGE)
        self.main.login = False
        self.main.admin = False
    def showItems(self, main):
        self.label_head.grid(column=0, row=0, columnspan=3)
        self.adm_stock_l.grid(column=0, row=1)
        self.adm_stock_c.grid(column=1, row=1)
        self.adm_stock_c.config(values = main.shares_dict.keys())
        self.adm_ncost_l.grid(column=0, row=2)
        self.adm_ncost.grid(column=1, row=2)
        self.adm_namount_l.grid(column=0, row=3)
        self.adm_namount.grid(column=1, row=3)
        self.adm_update_b.grid(column=0, row=4)
        self.back_b.grid(column=1, row=4)
        self.view_stock()
        self.view_f_text.grid(column=0, row=5, sticky='nsew', columnspan=2)
        self.view_scroll.grid(column=2, row=5, sticky='ns')
    def hideItems(self, main):
        self.label_head.grid_forget()
        self.adm_stock_l.grid_forget()
        self.adm_stock_c.grid_forget()
        self.adm_ncost_l.grid_forget()
        self.adm_ncost.grid_forget()
        self.adm_namount_l.grid_forget()
        self.adm_namount.grid_forget()
        self.adm_update_b.grid_forget()
        self.back_b.grid_forget()
        self.view_f_text.grid_forget()
        self.view_scroll.grid_forget()
    def update(self):
        stock_name = self.adm_stock.get()
        ncost = int(self.adm_ncost.get())
        namount = self.adm_namount.get()
        if ncost<0:
            showinfo(message='Enter valid cost, Please check data')
            self.adm_ncost.delete(0,END)
        elif namount == '':
            namount = '0'
        elif int(namount)<0:
            showinfo(message='Enter valid amount, Please check data')
            self.adm_namount.delete(0, END)

        elif stock_name not in self.main.shares_dict:
            if not self.new_stock:
                showinfo(message='Are you sure you want to add this new stock \n Check the details once again')
                self.new_stock= True
            else:
                self.main.shares_dict[stock_name] = {}
                self.main.shares_dict[stock_name]['cost'] = str(ncost)
                self.main.shares_dict[stock_name]['tot_amount'] = namount
                self.main.shares_dict[stock_name]['name'] = stock_name
                self.main.shares_dict[stock_name]['tot_sold'] = '0'
                self.new_stock = False
                buff = {'tot_owned': '0', 'name': stock_name, 'money_spent': '0'}
                for name in self.main.users_dict:
                    self.main.users_dict[name].append(buff)
                self.adm_namount.delete(0,END)
                self.adm_ncost.delete(0,END)
                self.view_stock()
                self.adm_stock.set('')

        else:
            self.main.shares_dict[stock_name]['cost'] = str(ncost)
            tot_amount = int(self.main.shares_dict[stock_name]['tot_amount'])
            self.main.shares_dict[stock_name]['tot_amount'] = str(tot_amount+int(namount))
            self.adm_namount.delete(0,END)
            self.adm_ncost.delete(0,END)
            self.view_stock()
    def view_stock(self):
        self.view_f_text.config(state='normal')
        self.view_f_text.delete('1.0', 'end')
        key = self.main.shares_dict.keys()
        for name in key:
            li = self.main.shares_dict[name]
            txt_b1 = ' '*10+'Name: '
            self.view_f_text.insert('end',txt_b1)
            self.view_f_text.insert('end',name+'\n')
            txt_b2 = ' '*10+'Cost Price: '
            self.view_f_text.insert('end',txt_b2)
            self.view_f_text.insert('end',li['cost']+'\n')
            available_num = int(li['tot_amount']) - int(li['tot_sold'])
            txt_b3 = ' '*10+'Available amount: '
            self.view_f_text.insert('end',txt_b3)
            self.view_f_text.insert('end',str(available_num)+'\n')
            txt_b4 = ' '*10+'*'*20
            self.view_f_text.insert('end','\n'+txt_b4+'\n\n')
        self.view_f_text.config(state='disabled')