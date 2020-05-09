'''
Created on 2020/05/05

@author: YutoToguchi
'''

import threading

class ThreadClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print('************************** ThereadClass init **************************')
        self.__connections = threading.local()
        try:
            cache = self.__connections.cache
        except AttributeError:
            print('AttributeError')
            cache = self.__connections.cache ={}

        #key = (1, 2, 3, 4)
        #cache = [[1, 2, 3, 4]]
        #client = cache[key]
        #print(client)




