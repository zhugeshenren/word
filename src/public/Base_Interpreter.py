from abc import abstractmethod,ABCMeta

'''
    i definition a base interpreter , it's a parent class of all the interpreter , it should have three function :
    1. exec(*arg) : it has a group of parameters
    2.
'''

class BaseInterpreter(object):

    @abstractmethod
    def exec(self,*arge):pass

    @abstractmethod
    def multiThreadingExec(self,*args):pass

    @abstractmethod
    def singleThreadingExec(self,*args):pass

    @abstractmethod
    def otherExec(self,*args): pass
