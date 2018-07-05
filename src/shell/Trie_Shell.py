from src.public.Trie import Trie
from src.public.Trie import TrieNode

'''
    this is Trie of shell
'''

class TrieNodeOfShell(TrieNode):
    _interpreter = None
    _elem = None

    def __init__(self):
        self._elem = list()

    def getInterpreter(self):
        return self._interpreter

    def insert(self,values):
        self._elem.append(values)

    def delete(self, values):
        tNode = self.find(values)
        if tNode is None:
            return False
        else:
            self._elem.remove(tNode)
            return True

    def find(self,values):
        for i in range(0,len(self._elem)):
            if(self._elem[i]._value is values):
                return self._elem[i]
        return None

    def getLen(self):
        return len(self._elem)

class TrieOfShell(Trie):
    _heard = None

    def __init__(self):
        self._heard = TrieNodeOfShell()

    #be careful all key is character.
    def insert(self,key,values):
        keyLen = len(key)
        pNode = self._heard

        for i in range(0,keyLen):
            tNode = pNode.find(key[i])
            if tNode is None:
                iNode = TrieNodeOfShell()
                iNode._value = key[i]
                pNode.insert(iNode)
                pNode = iNode;
            else:
                pNode = tNode
        pNode._interpreter = values



    # Unavoidable use of recursion
    def delete(self,key):
        self._delete(key,0,self._heard)

    # private function
    def _delete(self,key,index,tNode):
        if index >= len(key):
            return

        fNode = tNode

        tNode = tNode.find(key[index])
        if tNode is None:
            return
        else:
            self._delete(key,index+1,tNode)

            if index == len(key) - 1:
                tNode._interpreter = None

            # Destroy object
            if tNode.getLen() is 0 and (tNode._interpreter is None):
                fNode.delete(key[index])
                del tNode

    def find(self,key):
        keyLen = len(key);
        pNode = self._heard
        for i in range(0,keyLen):
            tNode = pNode.find(key[i])
            if tNode is None:
                return tNode
            pNode = tNode

        return pNode


    # test function
    def _print(self,key):
        keyLen = len(key)
        tNode = self._heard

        for i in range(0,keyLen):
            tNode = tNode.find(key[i])
            if(tNode is None):
                return "error"
        print(tNode._interpreter)





