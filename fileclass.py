'''
Created on 2020/05/06

@author: YutoToguchi
'''

class FileClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        print(params)

    def write_file(self):
        print('************************** open_file **************************')
        f = open('file.txt', 'w')
        f.write('Hellow!\n')
        f.write('How are you?\n')
        f.close

        pass

