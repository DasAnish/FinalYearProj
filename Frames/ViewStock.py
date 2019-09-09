from tkinter import Text, Scrollbar, VERTICAL
from tkinter.ttk import Frame, Label, Button
from tkinter.messagebox import showinfo

LARGE_FONT = ('Comic Sans MS', 20)
MED_FONT = ('Comic Sans MS', 15)
SMALL_FONT = ('Comic Sans MS', 10)
ADMIN_PAGE, LOGIN_PAGE, RETAIL_PAGE, SIGN_UP_PAGE, VIEW_STOCK = [0, 1, 2, 3, 4]




class viewStock(Frame):
    '''The Frame that is kind of a logged in view and contains buttons
        to move to sell, buy or log out. At the same time it
        it also shows what stocks one has along with their profit and more'''
    def __init__(self, parent, main, **kw):
        Frame.__init__(self, parent, **kw)
        self.view_f_text = Text(width=30)
        self.main = main
        self.view_scroll = Scrollbar(orient = VERTICAL, command=self.view_f_text.yview)
        self.view_f_text.config(yscrollcommand = self.view_scroll.set)
        self.label_head = Label(text='Stocks available', font = MED_FONT)
        self.back_b = Button(text='Login and Buy', command = self.back )
        self.buy_b = Button(text='BUY', command = self.buy)
        self.sell_b = Button(text='SELL', command = self.sell)
    def buy(self):
        '''the call back if we click on buy and takes us to the buy window'''
        self.main.frames[RETAIL_PAGE].page = 'b'
        self.main.show_frame(RETAIL_PAGE, VIEW_STOCK)
    def sell(self):
        '''the call back if we click on sell and it takes us to the sell window'''
        self.main.frames[RETAIL_PAGE].page = 's'
        self.main.show_frame(RETAIL_PAGE, VIEW_STOCK)
    def back(self):
        '''this is kind of the '''
        self.main.show_frame(LOGIN_PAGE, VIEW_STOCK)
        self.main.login = False
        self.main.admin = False
    def showItems(self, main):
        if main.login:
            self.back_b.config(text='Log Out')
            self.label_head.config(text='Logged in as %s'%self.main.present_user)
            self.buy_b.grid(column=0, row=2, columnspan=2)
            self.sell_b.grid(column=0, row=3, columnspan=2)
        else:
            self.back_b.config(text='Login and Buy')
            self.label_head.configure(text='View Stock')

        self.label_head.grid(column=0, row=0, columnspan=2)
        self.view_f_text.grid(column=0, row=1, sticky='nsew')
        self.view_scroll.grid(column=2, row=1)
        self.back_b.grid(column=0, row=4, columnspan=2)
        self.view_stock()
    def hideItems(self, main):
        self.label_head.grid_forget()
        self.view_f_text.grid_forget()
        self.view_scroll.grid_forget()
        self.back_b.grid_forget()

        if main.login:
            self.buy_b.grid_forget()
            self.sell_b.grid_forget()
    def view_stock(self):
        self.view_f_text.config(state='normal')
        self.view_f_text.delete('1.0', 'end')

        if self.main.login and not self.main.admin:
            l2 = self.main.accounts[self.main.present_user]
            txt_1 = 'Balance: ' + l2['balance'] + '\n' + 'Profit: ' + l2['profit'] + '\n'*2 + '*'*20 + '\n'
            self.view_f_text.insert('end',txt_1)
        key = self.main.shares_dict.keys()

        if not self.main.login:
            for name in key:
                li = self.main.shares_dict[name]
                txt_b1 = 'Name: '
                self.view_f_text.insert('end',txt_b1)
                self.view_f_text.insert('end',name+'\n')
                txt_b2 = 'Cost Price: '
                self.view_f_text.insert('end',txt_b2)
                self.view_f_text.insert('end',li['cost']+'\n')
                available_num = int(li['tot_amount']) - int(li['tot_sold'])
                txt_b3 = 'Available amount: '
                self.view_f_text.insert('end',txt_b3)
                self.view_f_text.insert('end',str(available_num)+'\n')
                txt_b4 = '*'*20
                self.view_f_text.insert('end','\n'+txt_b4+'\n\n')
        self.view_scroll.grid(column=1, row=0, rowspan=2, sticky='nswe')

        if self.main.login:
            for name in key:
                li = self.main.shares_dict[name]
                txt_b1 = 'Name: '
                self.view_f_text.insert('end',txt_b1)
                self.view_f_text.insert('end',name+'\n')
                txt_b2 = 'Cost Price: '
                self.view_f_text.insert('end',txt_b2)
                self.view_f_text.insert('end',li['cost']+'\n')
                available_num = int(li['tot_amount']) - int(li['tot_sold'])
                txt_b3 = 'Available amount: '
                self.view_f_text.insert('end',txt_b3)
                self.view_f_text.insert('end',str(available_num)+'\n')
                lis =  self.main.p_user_dict
                for i in lis:
                    if i['name'] == name:
                        lis = i
                        break
                txt1 = 'Stocks owned: '+lis['tot_owned']+'\n' if not lis['tot_owned'] == '0' else ''
                self.view_f_text.insert('end', txt1)
                txt2 = 'Money spent: '+ lis['money_spent']+'\n' if not lis['tot_owned'] == '0' else ''
                self.view_f_text.insert('end', txt2)
                txt_b4 = '*'*20
                self.view_f_text.insert('end','\n'+txt_b4+'\n\n')
            self.view_f_text.config(state='disabled')
        else:
            self.view_f_text.config(state='disabled')