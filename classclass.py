'''
Created on 2020/05/05

@author: YutoToguchi
'''

class ClassClass(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        print(params)

    def method(self):
        print('************************** method **************************')
        print(self.__class__)
        print()

    @classmethod
    def class_method(cls):
        print('************************** class_method **************************')
        print(cls.__class__)
        print()

    @staticmethod
    def static_method():
        print('************************** static_method **************************')
        print(ClassClass.__class__)
        print()

    def start(self):
        pass
