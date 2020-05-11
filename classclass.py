'''
Created on 2020/05/05

@author: YutoToguchi
'''

class ClassClass(object):
    '''
    classdocs
    '''
    # クラス変数
    __counter = 0

    def __init__(self, params, name = 'ClassTest', capsule_value = 100):
        '''
        Constructor
        '''

        ClassClass.__counter += 1

        # インスタンス変数
        self.__name = name
        self.__capsule_value = capsule_value
        self.__id = ClassClass.__counter

        print(params)

    def __str__(self) -> str:
        print('************************** __str__ **************************')
        return self.__name

    def printstr(self) -> None:
        print('************************** printstr **************************')
        print(self.__str__())

    def method(self) -> None:
        print('************************** method **************************')
        print(self.__class__)
        print(self.__name)
        print()

    @classmethod
    def class_method(cls) -> None:
        print('************************** class_method **************************')
        print(cls.__class__)
        print(cls.__counter)
        print()

    @staticmethod
    def static_method() -> None:
        print('************************** static_method **************************')
        print(ClassClass.__class__)
        print(ClassClass.__counter)
        print()

    @property
    def capsule_value(self) -> int:
        '''
        propertyを設定するとcapsule_value()の代わりにcapsule_valueで呼び出すことができる。これをpropertyデコレータという。
        '''
        print('************************** capsule_value getter **************************')
        print(self.__capsule_value)
        return self.__capsule_value

    @capsule_value.setter
    def capsule_value(self, capsule_value: int) -> None:
        '''
        capsule_value.setterを設定するとcapsule_value()の代わりにcapsule_valueで呼び出すことができる。
        '''
        print('************************** capsule_value setter **************************')
        self.__capsule_value = capsule_value

    @property
    def id(self) -> None:
        print('************************** id getter **************************')
        print(self.__id)
        return self.__id

# Complete Class

