'''
Created on 2020/05/06

@author: YutoToguchi
'''

class SetClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

    def create_set(self):
        print('************************** create_set **************************')
        set01 = {1}
        set02 = {1, 2, 3}
        set03 = {1, 2, 3,}
        set04 = {'Japan', 'America', 'Australie'}
        set05 = set()
        set06 = set('JapanJapanJapan')
        set07 = set([1, 2, 3])
        set08 = set([1, 2, 3,])
        set09 = ((1, 2, 3))
        set10 = set('123123123')
        print('set01:', set01)
        print('set02:', set02)
        print('set03:', set03)
        print('set04:', set04)
        print('set05:', set05)
        print('set06:', set06)
        print('set07:', set07)
        print('set08:', set08)
        print('set09:', set09)
        print('set10:', set10)

        lst1 = [1, 2, 3, 4, 3, 2]
        lst2 = set(set(lst1))

        print('lst1', lst1)
        print('lst2', lst2)

        set11 = {n for n in range(1, 8)}
        print(set11)

        print()

    def show_set(self):
        pass

    def compare_set(self):
        print('************************** compare_set **************************')
        set01 = {1, 2, 3}
        set02 = {3, 1, 2}
        set03 = {2, 3, 1, 1, 1, 1}
        print('set01:', set01)
        print('set02:', set02)
        print('set03:', set03)
        print(set01 == set02 == set03)
        print('set01 id:{}, set02 id:{}'.format(id(set01), id(set02)))

        print(1 in set01)
        print(100 in set01)
        print(100 not in set01)
        print(set01 in set02)
        for i in set01:
            print('{}(a part of set01) in {}(set02) is {}'.format(i, set02, i in set02))

        for i, element in enumerate(set01):
            print(i, element)

        print()

    def operation_set(self):
        print('************************** operation_set **************************')
        s1 = {1, 2, 3, 4, 5, 6}
        print(s1)
        s1.add(1000)
        print(s1)
        s1.discard(1)
        print(s1)
        e = s1.pop()
        print(e, s1)
        e = s1.pop()
        print(e, s1)
        s1.clear()
        print(s1)

        s2 = {1, 2, 3}
        s3 = {4, 5, 6}
        print(s2.isdisjoint(s3))
        print(s2.issubset(s3))




        print()


