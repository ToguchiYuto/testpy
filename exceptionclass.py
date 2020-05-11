'''
Created on 2020/05/10

@author: YutoToguchi
'''

import sys
import traceback


class MyExceptionClass(Exception):
    pass

class ExceptionClass():
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        print(params)

    def raise_my_exception(self) -> None:
        '''
        MyExceptionClassをraiseする。
        '''
        raise MyExceptionClass

    def calc(self, value1: int = 10, value2: int = 0) -> None:
        print('************************** calc **************************')

        if(value2 == 0):
            '''
            呼び出しもとの関数にZeroDivisionErrorを返す。
            この場合、即座に関数はraiseして終了する。
            '''
            raise ZeroDivisionError

        try:
            print(value1 / value2)
        except ZeroDivisionError as e:
            print('print Zero Division Error')

            print('type:',type(e))
            print()

            print(traceback.format_exc())
            print()

            type_, value, traceback_ = sys.exc_info()
            print('type_:',type_)
            print('value:',value)
            print('traceback:',traceback_)
            print()

            print(traceback.format_exception(type_, value, traceback_))
            print()
        except ValueError:
            print('print Value Error')
        except:
            '''
            例外の種類を指定しない場合に実行される。すべての例外を補足することができる。
            '''
            print('print except')
        else:
            '''
            どのexceptにも補足されなかった場合に実行される。
            '''
            print('Success')
        finally:
            '''
            必ず最後に実行される。
            '''
            print('print finally')

    def calc_myexcept(self, value1: int = 10, value2: int = 0) -> None:
        print('************************** calc **************************')

        try:
            if(value2 == 0):
                '''
                このifに入った場合、raise_my_exception()関数が実行される。
                関数が実行されるとMyExceptionClassがraiseされ、MyExceptionClassでキャッチされる。
                '''
                self.raise_my_exception()

            print(value1 / value2)

        except MyExceptionClass as e:
            '''
            MyExceptionClassをキャッチすると上位の関数へExceptionをraiseする。
            '''
            print(type(e))
            raise Exception

        except:
            print('print except')

        finally:
            print('print finally')

    # Complete
