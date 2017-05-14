from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import os

def ftpServer(user, psw, port=2121, write=True):
    authorizer = DummyAuthorizer()
    if write == True:
    	authorizer.add_user(user, psw , '.', perm='elradfmwM')
    else:
    	authorizer.add_user(user, psw , '.')
    # authorizer.add_anonymous(os.getcwd())
    handler = FTPHandler
    handler.authorizer = authorizer
    server = ThreadedFTPServer(('0.0.0.0', port), handler)
    server.serve_forever()

if __name__ == "__main__":
    ftpServer('user', '123456', 2121, True)