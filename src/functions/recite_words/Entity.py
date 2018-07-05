class BaseEntity(object):
    pass

'''
    manage word
    File storage is not a concern at this level,  "decoupling" --- this is the key
    
    -  : table column name
    ---- : table name
    
    file format :
        book----
            - book name
            - book describe
            - book classify : the number of books classified
            - classify name : array describe

            
        classify----
            - classify name :
            - classify describe :
            - word count :
            - word block count :
            - word block : array describe
        
        wordBlock----
            - block name
            - block describe
            - world count
            - word : array describe
            
        word----
            - translate : chinese translation
            - part_of_speech : vt/v/vi/adj..
    
'''


class Book(BaseEntity):
    def __init__(self):
        # create attribute
        self.uid = None
        self.bookName = None
        self.bookDescribe = None
        self.bookClassify = None

class ClassifyList(BaseEntity):
    def __init__(self):
        #
        self.uid = None
        self.bookUid = None
        self.classifyUid = None


class BookClassify(BaseEntity):
    def __init__(self):
        # create attribute
        self.uid = None
        self.classifyName = None
        self.classifyDescribe = None
        self.wordBlockCount = None

class WordBlockList(BaseEntity):
    def __init__(self):
        #
        self.uid = None
        self.bookClassifyUid = None
        self.wordBlockUid = None


class WordBlock(BaseEntity):
    def __init__(self):
        self.uid = None
        self.blockName = None
        self.blockDescribe = None
        self.wordCount = None
        pass

class Word(BaseEntity):
    def __init__(self):
        self.uid = None
        self.blockUid = None

        self.translate = None
        self.part_of_speech = None
