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
# from classclass import classclass

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

# How to Use File
fc = FileClass()
fc.write_file()

# How to Use Method
mc = MethodClass('Method Class Init')
# mc.start()

# How to Use Class
cc = ClassClass('Class Class Init')
cc.start()











if __name__ == '__main__':
    pass