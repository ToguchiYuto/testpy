'''
Created on 2020/05/05

@author: YutoToguchi
'''

class TupleClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

    def show_tuple_list(self):
        print('************************** show_tuple_list **************************')
        students = [
            (123, 'YutoToguchi'),
            (456, 'YutoToguchi1'),
            (678, 'YutoToguchi2')
            ]

        print('students', students)

        for i in students:
            print(i)
        print()

        for i in range(len(students)):
            print('ID:{} NAME:{}'.format(students[i][0], students[i][1]))
        print()


    def show_tuple_zip(self):
        print('************************** show_tuple_zip **************************')
        t1 = (123, 'YutoToguchi')
        t2 = (456, 'YutoToguchi1')
        tz = tuple(zip(t1,t2))
        print(tz)
        print(type(zip(t1, t2)))

        print()


