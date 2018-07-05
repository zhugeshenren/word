from src.shell.Trie_Shell import TrieOfShell

class Test:
    def exec(self,*arg):
        print(arg)

if __name__=='__main__':
    ts = TrieOfShell()
    test = Test()

    ts.insert('zhu',test)
    ts.find('zhu').getInterpreter().exec('zhuge1995')
