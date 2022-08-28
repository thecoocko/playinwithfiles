import os, sys
from subprocess import call
from stat import *

class SearchFile():
    def __init__(self,top,callback):
        self.__top = top
        self.__callback = callback

    @property
    def top(self,top):
        return self.__top
    @property
    def callback(self,callback):
        return self.__callback
    @top.setter
    def top(self,top):
        self.__top = top
    @callback.setter
    def callback(self,callback):
        self.__callback = callback
    
    def search(self,top, callback):
        for f in os.listdir(top):
            pathname = os.path.join(top, f)
            mode = os.lstat(pathname).st_mode
            if S_ISDIR(mode):
                # It's a directory, recurse into it
                self.search(pathname, callback)
            elif S_ISREG(mode):
                # It's a file, call the callback function
                callback(pathname)
            else:
                # Unknown file type, print a message
                print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)

print(walktree('D:\\рандом параша\\trainproject',visitfile))