'''
Created on 2020/05/05

@author: YutoToguchi
'''
from TupleClass import TupleClass
from DictClass import DictClass
from SetClass import SetClass
from FileClass import FileClass
#from ClassClass import ClassClass
#from ThreadClass import ThreadClass


tc = TupleClass()
tc.show_tuple_list()
tc.show_tuple_zip()

dc = DictClass()
dc.create_dict()
dc.compare_dict()
dc.show_dict()
dc.operation_dict()
dc.operation_setdecault()
dc.operation_update()

sc = SetClass()
sc.create_set()
sc.compare_set()
sc.operation_set()

fc = FileClass()
fc.write_file()






'''
cc = ClassClass()
print(cc, type(cc), id(cc))

print(cc.method)
print(cc.class_method)
print(cc.static_method)
print(setattr(ClassClass, "value", "10"))
print(getattr(ClassClass, "value"))
getattr(ClassClass, "class_method")()

print(ClassClass, type(ClassClass), id(ClassClass))
print(ClassClass.method)
print(ClassClass.class_method)
print(ClassClass.static_method)

th = ThreadClass()
'''





if __name__ == '__main__':
    pass