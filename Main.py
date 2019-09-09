from tkinter import Tk, Frame
from Util.GetData import getData
LARGE_FONT = ('Comic Sans MS', 20)
MED_FONT = ('Comic Sans MS', 15)
SMALL_FONT = ('Comic Sans MS', 10)

ADMIN_PAGE, LOGIN_PAGE, RETAIL_PAGE, SIGN_UP_PAGE, VIEW_STOCK = [0, 1, 2, 3, 4]

from Frames.LoginPage import loginPage
from Frames.SignUpPage import signUpPage
from Frames.ViewStock import viewStock
from Frames.AdminPage import adminPage
from Frames.RetailPage import retailPage


class main_(Tk, getData):
    '''The main class of this project. It inherits from Tk and getData.
It contains instances of the all the frames that are used and thus the frames have a Has-A relationship
'''

    def __init__(self, *args, **kwargs):
        ##        print 'Execution started'
        getData.__init__(self)
        Tk.__init__(self, *args, **kwargs)

        ##        print 'Window created'
        self.login = not False
        self.present_user = ''
        self.p_user_dict = {} if self.present_user == '' else self.users_dict[self.present_user]
        self.admin = False
        container = Frame(self)
        container.grid(column=0, row=0)

        self.frames = {LOGIN_PAGE: loginPage(container, self),
                       VIEW_STOCK: viewStock(container, self),
                       SIGN_UP_PAGE: signUpPage(container, self),
                       RETAIL_PAGE: retailPage(container, self),
                       ADMIN_PAGE: adminPage(container, self)}

        self.show_frame(LOGIN_PAGE, None)

    def show_frame(self, newFrame, oldFrame=None):
        '''This function is quite important because all the frames use this to change frames
'''
        frame = self.frames[newFrame]
        frame.showItems(self)
        if not oldFrame == None:
            old = self.frames[oldFrame]
            old.hideItems(self)

        frame.tkraise()

if __name__ == "__main__":
    app = main_()
    app.mainloop()
    app.export()