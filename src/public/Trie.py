from abc import abstractmethod, ABCMeta

'''
    This is Trie , i need a shell command parsing tool , but it should be a subclass of Trie.
    In another way, all character lookup classes take it as the parent class
'''


class Trie(object):
    @abstractmethod
    def insert(self, key, values): pass

    @abstractmethod
    def delete(self, key): pass

    @abstractmethod
    def find(self, key): pass

    @abstractmethod
    def update(self, key, values): pass


'''
    TrieNode is tree node
    Genericity allows me
'''


class TrieNode(object):
    _elem = None
    _value = None

    @abstractmethod
    def insert(self, values): pass

    @abstractmethod
    def delete(self, values): pass

    @abstractmethod
    def find(self, values): pass

    @abstractmethod
    def getLen(self): pass
