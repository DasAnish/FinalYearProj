from tkinter import Frame, END
from tkinter.ttk import Label, Button, Entry, Frame
from tkinter.messagebox import showinfo

LARGE_FONT = ('Comic Sans MS', 20)
MED_FONT = ('Comic Sans MS', 15)
SMALL_FONT = ('Comic Sans MS', 10)
ADMIN_PAGE, LOGIN_PAGE, RETAIL_PAGE, SIGN_UP_PAGE, VIEW_STOCK = [0, 1, 2, 3, 4]

class loginPage(Frame):
    ''' This is a frame class and thus it implements Frame,
        it also contains the required showItems and hideItems function which I believe are present in each frame class
        tomake things a bit simpler
'''
    def __init__(self, parent, main, **kw):
        Frame.__init__(self, parent, **kw)
        self.main = main
        self.label_head = Label(text='Welcome to the Stock Exchange', font = LARGE_FONT)
        self.l_user = Label(text='Username')
        self.user = Entry()
        self.l_pass = Label(text='Password')
        self.password = Entry(show='*')
        self.login_back_b = Button(text='Login', command= lambda: self.login_check())
        self.sign_up_b = Button(text='Sign Up', command = lambda: self.main.show_frame(SIGN_UP_PAGE, LOGIN_PAGE))
        self.view_stock_b = Button(text='View Stock', command = lambda: self.main.show_frame(VIEW_STOCK, LOGIN_PAGE))
        self.main.bind('<Return>', self.keyPress)
    def showItems(self, main):
        self.label_head.grid(column=0, row=0, columnspan=2)
        self.l_user.grid(column=0, row=1)
        self.user.grid(column=1, row=1)
        self.l_pass.grid(column=0, row=2)
        self.password.grid(column=1, row=2)
        self.login_back_b.grid(column=0, row=3, columnspan=2)
        self.sign_up_b.grid(column=0, row=4)
        self.view_stock_b.grid(column=1, row=4)
    def hideItems(self, main):
        self.label_head.grid_forget()
        self.l_user.grid_forget()
        self.user.grid_forget()
        self.l_pass.grid_forget()
        self.password.grid_forget()
        self.login_back_b.grid_forget()
        self.sign_up_b.grid_forget()
        self.view_stock_b.grid_forget()
    def keyPress(self, event):
        ''' this is the binding fucntion for any keyPress event
'''
        if event.keysym == 'Return':
            self.login_check()
    def login_check(self):
        ''' This function checks whether a given user is registered on the system or not
            then continues to chech whether they have entered the correct password.
            it also creates messagesboxes to give the proper error message to the user
'''
        main = self.main
        user = str(self.user.get())
        password = bytes(str(self.password.get()), 'utf-8')
        main.login= False
        check1 = user in main.pass_dict
        check3 = user == 'admin' and password == 'admin'
        if check1:
            check2 = main.pass_dict[user] == password
        if check1 and check2:
            main.login = True
        else:
            main.login = False
        if check3:
            main.login = True
            main.admin = True
            main.show_frame(ADMIN_PAGE, LOGIN_PAGE)
        if main.login:
            if not check3:
                main.present_user, main.p_user_dict = user, main.users_dict[user]
                main.show_frame(VIEW_STOCK, LOGIN_PAGE)
            self.password.delete(0,END)
            self.user.delete(0, END)
        else:
            self.password.delete(0,END)
            showinfo(message='Incorrect Username or Password entered')