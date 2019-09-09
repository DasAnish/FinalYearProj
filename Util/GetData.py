from pickle import load, dump
from base64 import b64encode as encode, b64decode as decode

class getData:
    ''' This is our first main parent class that implements the reading and writing to files
This class is inherited by our main class. It also decodes the passwords which are currently in encoded format
'''
    def __init__(self):
        '''The constructor that reads all the files and creates instance variables from them
'''
        __fs = open('share_file.dat', 'rb')
        self.shares_dict = load(__fs)
        __fs.close()

        __fu = open('user_file.dat', 'rb')
        self.users_dict = load(__fu)
        __fu.close()

        __fp = open('pass_file.dat', 'rb')
        self.pass_dict2 = load(__fp)
        self.pass_dict = {}
        for name in self.pass_dict2:
            self.pass_dict[name] = decode(self.pass_dict2[name])

        __fa = open('acc_file.dat', 'rb')
        self.accounts = load(__fa)
        __fa.close()

        print(self.shares_dict, self.users_dict, self.pass_dict, self.accounts)
    def export(self):
        ''' This function as the name suggestes exports i.e. writes the new files to the required files
'''
        __fs = open('share_file.dat', 'wb')
        dump(self.shares_dict, __fs)
        __fs.close()

        __fu = open('user_file.dat', 'wb')
        dump(self.users_dict, __fu)
        __fu.close()

        __fp = open('pass_file.dat', 'wb')
        dump(self.pass_dict2, __fp)
        __fp.close()

        __fa = open('acc_file.dat', 'wb')
        dump(self.accounts, __fa)
        __fa.close()