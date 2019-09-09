from tkinter import Tk, StringVar, END
from tkinter.ttk import Label, Button, Combobox, Entry, Frame
from tkinter.messagebox import showinfo

LARGE_FONT = ('Comic Sans MS', 20)
MED_FONT = ('Comic Sans MS', 15)
SMALL_FONT = ('Comic Sans MS', 10)
ADMIN_PAGE, LOGIN_PAGE, RETAIL_PAGE, SIGN_UP_PAGE, VIEW_STOCK = [0, 1, 2, 3, 4]



class retailPage(Frame):
    ''' the main page that actually branches into 2 seperate frames for buying and selling
        this frame provides the use with the
'''

    def __init__(self, parent, main, **kw):
        Frame.__init__(self, parent, **kw)
        self.main = main
        self.Head = Label(font=MED_FONT)

        self.retail_back_b = Button(text='BACK', command=self.back_fb)
        self.stock_name = StringVar()
        self.stock_name_ = ''
        self.stock_name_c = Combobox(textvariable=self.stock_name)
        self.stock_name_l = Label(text='Stock name: ')
        self.amount = Entry()
        self.amount_l = Label(text='Number of stocks :')

        self.check_avail_b = Button(text='Check')
        self.cost_l = Label(text='Cost: ')
        self.cost = Label()
        self.buy_stock_b = Button(text='BUY Stock')
        self.sellp_l = Label(text='Current Selling Price: ')
        self.profit_l = Label(text='PROFIT/LOSS')
        self.sell_stock_b = Button(text='SELL Stock')
        self.page = None

    def showItems(self, main):
        self.Head.grid(column=0, row=0, columnspan=2)
        self.Head.configure(text='logged in as %s' % main.present_user)
        if self.page == 'b':
            self.buy()
        elif self.page == 's':
            self.sell()

    def hideItems(self, main):
        self.Head.grid_forget()

    def buy(self):
        '''This function creates the buy window
'''
        self.retail_back_b.grid(column=1, row=5)
        self.retail_back_b.config(command=self.back_fb)
        self.stock_name_l.grid(column=0, row=1)
        self.stock_name_c.grid(column=1, row=1)
        self.stock_name_c.config(values=self.main.shares_dict.keys())
        self.amount_l.grid(column=0, row=2)
        self.amount.grid(column=1, row=2)
        self.check_avail_b.config(command=self.check_avail_buy)
        self.check_avail_b.grid(column=0, row=3)
        self.cost_l.grid(column=0, row=4, columnspan=2)
        self.buy_stock_b.config(command=self.buy_stock, text='Buy Stock', state='disabled')
        self.buy_stock_b.grid(column=0, row=5)

    def sell(self):
        '''This function creats the sell window'''
        self.retail_back_b.grid(column=1, row=6)
        self.retail_back_b.config(command=self.back_fs)
        self.check_avail_b.config(command=self.check_avail_sell)
        self.stock_name_l.grid(column=0, row=1)
        self.stock_name_c.grid(column=1, row=1)
        self.stock_name_c.config(values=self.main.shares_dict.keys())
        self.amount_l.grid(column=0, row=2)
        self.amount.grid(column=1, row=2)
        self.check_avail_b.grid(column=0, row=3)
        self.sellp_l.grid(column=0, row=4, columnspan=2)
        self.profit_l.grid(column=0, row=5, columnspan=2)
        self.sell_stock_b.config(command=self.sell_stock, state='disabled', text='Check')
        self.sell_stock_b.grid(column=0, row=6)

    def back_fb(self):
        '''Back from buy i.e. removes all the items needed to make buy'''
        self.retail_back_b.grid_forget()
        self.Head.grid(column=0, row=0, columnspan=2)
        self.stock_name_l.grid_forget()
        self.stock_name_c.grid_forget()
        self.amount_l.grid_forget()
        self.amount.grid_forget()
        self.check_avail_b.grid_forget()
        self.cost_l.grid_forget()
        self.buy_stock_b.grid_forget()
        self.buy_stock_b.config(state='disabled')

        self.main.show_frame(VIEW_STOCK, RETAIL_PAGE)
        self.stock_name.set('')
        self.amount.delete(0, END)

    def back_fs(self):
        ''' Back from sell i.e. removes all the items needed to make it sell window'''
        self.Head.grid(column=0, row=0, columnspan=2)
        self.retail_back_b.grid_forget()
        self.check_avail_b.grid_forget()
        self.stock_name_l.grid_forget()
        self.stock_name_c.grid_forget()
        self.amount_l.grid_forget()
        self.amount.grid_forget()
        self.sellp_l.grid_forget()
        self.profit_l.grid_forget()
        self.sell_stock_b.grid_forget()

        self.main.show_frame(VIEW_STOCK, RETAIL_PAGE)
        self.stock_name.set('')
        self.amount.delete(0, END)
        self.check_avail_b.grid_forget()

    def check_avail_buy(self):
        ''' Performs a check whether the number of shares requisted are available or not and then check whether the
            person has the required amounts of fund or not for the transaction to go through'''
        name = self.stock_name.get()
        l2 = self.main.accounts[self.main.present_user]

        if name in self.main.shares_dict.keys():
            li = self.main.shares_dict[name]
        else:
            self.stock_name.delete(0, END)
            showinfo(meassage='Enter a Valid Stock name')

        available_num = int(li['tot_amount']) - int(li['tot_sold'])
        req = int(self.amount.get())
        cost = req * int(li['cost'])

        if req < 0:
            showinfo(message='Enter a Valid amount')
        elif req > available_num:
            showinfo(message='Enter an amount less than ' + str(available_num))
        elif cost > int(l2['balance']):
            showinfo(message='You have only %s in you account' % l2['balance'])
        else:
            self.cost_l.config(text='Cost: \t' + li['cost'] + '*' + str(req) + '=' + str(cost))
            self.buy_stock_b.config(state='normal')

    def check_avail_sell(self):
        ''' Performs a check whether the user has enough stocks to sell'''
        name = self.stock_name.get()
        if name in self.main.shares_dict.keys():
            li = self.main.shares_dict[name]
        else:
            self.stock_name.delete(0, END)
            showinfo(message='Enter a Valid Stock name')
        req = int(self.amount.get())
        if req < 0:
            showinfo(message='Please Enter a Valid amount')
            self.amount.delete(0, END)
        li = self.main.p_user_dict
        ok = False
        for i in li:
            if name == i['name']:
                ok = True
                buff = i

        if req > int(buff['tot_owned']):
            showinfo(message='You dont have that many stocks try less than ' + buff['tot_owned'])
            self.amount.delete(0, END)
        cost = self.main.shares_dict[name]['cost']
        tot_cost = req * int(cost)
        try:
            spent = req * float(buff['money_spent']) / int(buff['tot_owned'])
        except:
            spent = 0
        pol = tot_cost - spent

        if pol >= 0:
            self.profit_l.config()
        elif pol < 0:
            self.profit_l.config()
        if req <= int(buff['tot_owned']):
            self.sellp_l.config(text='Current Selling Price: \t' + cost)
            self.profit_l.config(text="PROFIT-LOSS: \t" + str(pol))
            self.sell_stock_b.config(command=self.sell_stock, text='Sell Stock')
            showinfo(message='Everthing is ok, \nClicking Sell will execute the trade')
            self.sell_stock_b.config(state='normal')

    def buy_stock(self):
        '''Finally Executes the transaction and asks the user for conformation one last time'''
        name = self.stock_name.get()
        li = self.main.shares_dict[name]

        for i in range(len(self.main.p_user_dict)):
            if name == self.main.p_user_dict[i]['name']:
                index = i
        req = int(self.amount.get())
        tot_cost = req * int(li['cost'])
        self.main.shares_dict[name]['tot_sold'] = str(int(self.main.shares_dict[name]['tot_sold']) + req)
        self.main.p_user_dict[index]['tot_owned'] = str(int(self.main.p_user_dict[index]['tot_owned']) + req)
        self.main.p_user_dict[index]['money_spent'] = str(int(self.main.p_user_dict[index]['money_spent']) + tot_cost)
        self.main.users_dict[self.main.present_user][index] = self.main.p_user_dict[index]
        balance = int(self.main.accounts[self.main.present_user]['balance'])
        self.main.accounts[self.main.present_user]['balance'] = str(balance - tot_cost)
        self.cost_l.config(text='Cost: ')

        showinfo(message='You have just bought %s of the stock %s at the price %s' % (str(req), name, str(tot_cost)))
        self.stock_name.set('')
        self.main.show_frame(VIEW_STOCK, RETAIL_PAGE)
        self.back_fb()

    def sell_stock(self):
        '''Asks the user for conformation and then completes the transaction
        of selling, at this point the profit field is
        also updated'''
        name = self.stock_name.get()
        req = int(self.amount.get())

        li = self.main.p_user_dict
        for i in range(len(li)):
            if name == li[i]['name']:
                ok = True
                buff = i

        tot_cost = req * int(self.main.shares_dict[name]['cost'])
        try:
            spent = req * float(self.main.p_user_dict[buff]['money_spent']) / int(
                self.main.p_user_dict[buff]['tot_owned'])
        except ZeroDivisionError:
            spent = 0
        self.main.shares_dict[name]['tot_sold'] = str(int(self.main.shares_dict[name]['tot_sold']) - req)
        self.main.p_user_dict[buff]['tot_owned'] = str(int(self.main.p_user_dict[buff]['tot_owned']) - req)
        pol = tot_cost - spent
        diff = int(self.main.p_user_dict[buff]['money_spent']) - tot_cost
        self.main.p_user_dict[buff]['money_spent'] = str(diff) if diff > 0 else '0'
        self.main.users_dict[self.main.present_user] = self.main.p_user_dict
        profit = int(self.main.accounts[self.main.present_user]['profit'])
        self.main.accounts[self.main.present_user]['profit'] = str(int(profit + pol))
        balance = int(self.main.accounts[self.main.present_user]['balance'])
        self.main.accounts[self.main.present_user]['balance'] = str(balance + tot_cost)
        self.retail_back_b.grid_forget()
        self.profit_l.config(text='PROFIT/LOSS: ')
        self.sellp_l.config(text='Current selling price: ')
        self.main.show_frame(VIEW_STOCK, RETAIL_PAGE)
        self.back_fs()