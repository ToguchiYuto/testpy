'''
Created on 2020/05/05

@author: YutoToguchi
'''

from tupleclass import TupleClass
from dictclass import DictClass
from setclass import SetClass
from fileclass import FileClass
from methodclass import MethodClass
from classclass import ClassClass
from exceptionclass import ExceptionClass

# How to Use Tuple
tc = TupleClass()
tc.show_tuple_list()
tc.show_tuple_zip()

# How to Use Dictonary
dc = DictClass()
dc.create_dict()
dc.compare_dict()
dc.show_dict()
dc.operation_dict()
dc.operation_setdecault()
dc.operation_update()

# How to Use Set
sc = SetClass()
sc.create_set()
sc.compare_set()
sc.operation_set()



# How to Use Class
cc = ClassClass('Class Class Init', name = 'Class1')
cc1 = ClassClass('Class Class Init1', name = 'Class2')

'''
__を先頭につけた場合、外部のクラスからこの変数を参照できなくなる。
そのため、以下のような値を参照するような場合は、エラーとなる。
値にアクセスする場合は、カプセル化された変数を参照、変更するための関数をクラス内部に宣言しなければいけない。
# print(cc.__capsule_value)
'''
cc.capsule_value # __capsule_valueを取得するための関数をよびだす。通常の関数呼び出しでは()が必要だが、この場合は不要。
cc.capsule_value = 1000 # __capsule_valueに新しい値を設定する。
cc.capsule_value # __capsule_valueの値が変更されているか確認する。

'''
__str__へのアクセス
'''
print(str(cc))
cc.printstr()

'''
クラス変数へアクセス
クラス変数は、作成されたオブジェクトで共有される変数。一方、インスタンス変数は特定のオブジェクトの内部だけで利用される変数。
'''
cc.id
cc1.id

'''
インスタンスメソッド、クラスメソッド、スタティックメソッド
インスタンスメソッド：オブジェクト内で定義されているインスタンス変数を参照、変更するために利用する。
クラスメソッド：クラス内で定義されているクラス変数を参照、変更するために利用する。
スタティックメソッド：オブジェクトを宣言しなくてもクラス変数を参照することができる。
'''

cc.method() # インスタンスメソッド
cc1.method() # インスタンスメソッド
cc.class_method() # クラスメソッド
cc1.class_method() # クラスメソッド
ClassClass.static_method() # スタティックメソッド

print()

# How to Use Exception
ec = ExceptionClass('Exception Class Init')
try:
    ec.calc()
except BaseException as e:
    '''
    raiseされたExceptionを受け取る場合は、BaseExceptionのサブクラスかインスタンスである必要がある。
    '''
    print('print catch exception')
    print(type(e))

try:
    ec.calc_myexcept()
except Exception as e:
    '''
    raiseされたExceptionをキャッチして実行する。
    '''
    print('print catch exception')
    print(type(e))

print()

# How to Use File
fc = FileClass('File Class Init')
fc.write_file()
print()

# How to Use Method
mc = MethodClass('Method Class Init')
mc.start()
print()


if __name__ == '__main__':
    pass