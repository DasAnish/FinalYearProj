from tkinter import BooleanVar, END
from tkinter.ttk import Label, Button, Entry, Frame, Checkbutton
from tkinter.messagebox import showinfo

from Util.GetData import getData
LARGE_FONT = ('Comic Sans MS', 20)
MED_FONT = ('Comic Sans MS', 15)
SMALL_FONT = ('Comic Sans MS', 10)
ADMIN_PAGE, LOGIN_PAGE, RETAIL_PAGE, SIGN_UP_PAGE, VIEW_STOCK = [0, 1, 2, 3, 4]

from base64 import b64encode as encode
from random import randint

class signUpPage(Frame):
    ''' The user is taken to this Frame if they choose to sign up
        this class implements the Frame Class in Tkinter and contains the
        required functions that will allow it to work well in this project
'''
    def __init__(self, parent, main, **kw):
        Frame.__init__(self, parent, **kw)
        self.main = main
        self.label_head = Label(text='Sign Up Page', font = MED_FONT)
        self.l_user = Label(text='Username')
        self.user = Entry(text='must have atleast 5 chars')
        self.l_pass = Label(text='Password')
        self.l_pass2 = Label(text='re-enter')
        self.password = Entry(show='*')
        self.password2 = Entry(show='*')
        self.sign_up_b = Button(text='Sign Up', command= lambda: self.sign_up(main))
        self.back_b = Button(text='Back',
                             command = lambda: self.main.show_frame(LOGIN_PAGE, SIGN_UP_PAGE))
        self.age = BooleanVar()
        self.age_c = Checkbutton(text='Are you above 16 years of age', variable=self.age, onvalue=True, offvalue=False)
        self.balance = BooleanVar()
        self.balance_c = Checkbutton(text='Do you have 10000 rupees in \nyour bank account',
                                     variable=self.balance, onvalue=True, offvalue=False)
    def showItems(self, main):
        self.label_head.grid(column=0, row=0, columnspan=2)
        self.l_user.grid(column=0, row=1)
        self.user.grid(column=1, row=1)
        self.l_pass.grid(column=0, row=2)
        self.l_pass2.grid(column=0, row=3)
        self.password.grid(column=1, row=2)
        self.password2.grid(column=1, row=3)
        self.age_c.grid(column=0, columnspan=2, row=4)
        self.balance_c.grid(column=0, columnspan=2, row=5)
        self.sign_up_b.grid(column=0, row=6, columnspan=2)
        self.back_b.grid(column=0, row=7, columnspan=2)
    def hideItems(self, main):
        self.label_head.grid_forget()
        self.l_user.grid_forget()
        self.user.grid_forget()
        self.l_pass.grid_forget()
        self.l_pass2.grid_forget()
        self.password.grid_forget()
        self.password2.grid_forget()
        self.sign_up_b.grid_forget()
        self.back_b.grid_forget()
        self.age_c.grid_forget()
        self.balance_c.grid_forget()
    def sign_up(self, main):
        ''' Similar to the login check function it does the necessary checks to make sure that a person actually is
            above 18 (not really) and has the required amount of money to open an account on this platform
            also it creates pop ups when ever an exceptional circumstance is reached
'''
        password1 = self.password.get()
        password2 = self.password2.get()
        username = self.user.get()
        bool1 = username not in main.users_dict.keys()
        bool2 = (password1 == password2)
        bool3 = len(password1) >= 5
        bool4 = username == 'admin'
        bool5 = self.age.get()
        bool6 = self.balance.get()

        if not bool1:
            num = str(randint(100,999))
            showinfo(message='Username already exists, try: '+username + num)
            self.password.delete(0,END)
            self.password2.delete(0,END)
        elif not bool2:
            showinfo(message='Passwords dont match')
            self.password.delete(0,END)
            self.password2.delete(0,END)
        elif not bool3:
            showinfo(message='Password must be more than 5 characters')
            self.password.delete(0,END)
            self.password2.delete(0,END)
        elif bool4:
            showinfo(message='Please don\'t use that username it is reserved')
        elif not bool5:
            showinfo(message='You must be 16 years or older to join')
        elif not bool6:
            showinfo(message='You need to have 10000 to create an account')

        else:
            buff = []
            for name in main.shares_dict.keys():
                temp = {}
                temp['name'] = name
                temp['tot_owned'] = '0'
                temp['money_spent'] = '0'
                buff.append(temp)
            self.main.users_dict[username] = buff
            self.main.pass_dict[username] = bytes(password1, 'utf-8')
            k = getData.key()
            self.main.pass_dict2[username] = encode(bytes(password1, 'utf-8'))
            self.main.accounts[username] = {'balance':str(10**4), 'profit':'0'}
            self.main.present_user = username
            self.main.p_user_dict = self.main.users_dict[username]
            self.main.login = True
            self.main.show_frame(VIEW_STOCK, SIGN_UP_PAGE)
            self.password.delete(0,END)
            self.password2.delete(0,END)
            self.user.delete(0, END)