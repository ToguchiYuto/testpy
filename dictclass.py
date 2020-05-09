'''
Created on 2020/05/05

@author: YutoToguchi
'''

class DictClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

    def create_dict(self):
        print('************************** create_dict **************************')
        dict01 = {}
        dict02 = {'Japan': 1, 'America': 2, 'Australia': 3}
        dict03 = dict()
        dict04 = dict([('Japan', 1), ('America', 2), ('Australia', 3)])

        print(dict01)
        print(dict02)
        print(dict03)
        print(dict04)
        print()

    def compare_dict(self):
        print('************************** compare_dict **************************')
        dict01 = {'Japan': 1, 'Australia': 3, 'America': 2}
        dict02 = {'Japan': 1, 'America': 2, 'Australia': 3}
        print(dict01)
        print(dict02)
        print(dict01 == dict02) # the result is true, not false
        print()

    def show_dict(self):
        print('************************** show_dict **************************')
        dict01 = {'Japan': 1, 'Australia': 3, 'America': 2}
        print(dict01['Japan'])
        # print(dict01['United Kingdom']) # Show Traceback
        print(dict01.get('Japan'))
        print(dict01.get('United Kingdom'))
        print()

    def operation_dict(self):
        print('************************** operation_dict **************************')
        dict01 = {'Japan': 1, 'America': 2, 'Australia': 3}
        print(dict01)
        dict01['Japan'] = 100
        print(dict01)
        dict01['United Kingdom'] = 4
        print(dict01)
        print()

    def operation_setdecault(self):
        print('************************** operation_setdecault **************************')
        dict01 = {'Japan': 1, 'America': 2, 'Australia': 3}
        print(dict01)
        value1 = dict01.setdefault('Japan', 1)
        print(value1)
        value2 = dict01.setdefault('United Kingdom', 4)
        print(value2)
        print(dict01)
        print()

    def operation_update(self):
        print('************************** operation_update **************************')
        dict01 = {'Japan': 1, 'America': 2, 'Australia': 3}
        dict02 = {'China': 1, 'Thai': 2}
        print('dict01:',dict01)
        print('dict02:',dict02)
        dict01.update(dict02)
        print('dict01:',dict01)
        print()

        dict03 = {'Japan': 1, 'America': 2, 'Australia': 3}
        dict04 = {'China': 1, 'Thai': 2, 'Japan': 3}
        print('dict03:',dict03)
        print('dict04:',dict04)
        dict03.update(dict04)
        print(dict03)
        print()

        dict05 = {'Japan': 1, 'America': 2, 'Australia': 3}
        print(dict05)
        dict05.update(America=4)
        print(dict05)
        print()










