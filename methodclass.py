'''
Created on 2020/05/09

@author: YutoToguchi
'''

class MethodClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        print(params)

    def _print_asterisk(self, n):
        # print('************************** print_asterisk **************************')
        for _ in range(n):
            print('*', end=' ')
        print()

    def _max2(self, val1, val2):
        return (val1, val2) if val1 > val2 else (val2, val1)

    def _max3(self, val1, val2, val3):
        max = val1
        if max < val2: max = val2
        if max < val3: max = val3
        return max

    def _calc_factrial(self, val):
        if val == 0:
            return 1
        else:
            return val * self._calc_factrial( val - 1)

        pass

    def _refid_val(self, val):
        print('val id:{} and value {} in _refid_val method'.format(id(val), val))
        val += 1
        print('val id:{} and value {} in _refid_val method after increment'.format(id(val), val))
        return val

    def _replace_value_list(self, replace_list, index, value):
        replace_list[index] = value

    def _reverse_list(self, reverse_list):
        length = len(reverse_list)
        split_length = length // 2
        print(split_length)

        for i in range(split_length):
            reverse_list[i], reverse_list[length - i - 1] = reverse_list[length - i - 1], reverse_list[i]




    def start(self):
        self._print_asterisk(10)

        # Make Tryangle
        print('************************** Make Tryangle **************************')
        tryangle_length = 5
        for i in range(1, tryangle_length + 1):
            self._print_asterisk(i)

        # Make square
        print('************************** Make Square **************************')
        square_length = 5
        for _ in range(1, square_length + 1):
            self._print_asterisk(square_length)

        # Find max value in 3 values
        print('************************** Find max value in 3 values **************************')
        print(self._max3(10, -1, 100))

        # Compare values
        print('************************** Compare values **************************')
        max, min = self._max2(1000, 10)
        print('Max:{} Min:{}'.format(max, min))

        # Calculation Factrial
        print('************************** Calculation Factrial **************************')
        print(self._calc_factrial(4))

        # Object Id Reference
        print('************************** Object Id Reference **************************')
        refid = 1000
        print('refid:{} and value {} before calling _refid_val method'.format(id(refid), refid))
        return_refid = self._refid_val(refid)
        print('refid:{} and value {} after calling _refid_val method'.format(id(refid), refid))
        print('return_refid:{} and value {} after calling _refid_val method'.format(id(return_refid), return_refid))

        # Replace value in list
        print('************************** Replace value in list **************************')
        replace_list = [10, 20, 30, 40, 50]
        for i in replace_list:
            print(i, end=' ')
        print()

        print('replace_list id {} before calling _replace_value_list'.format(id(replace_list)))
        self._replace_value_list(replace_list, 0, 60)

        for i in replace_list:
            print(i, end=' ')
        print()
        print('replace_list id {} after calling _replace_value_list'.format(id(replace_list)))

        # Reverse list
        print('************************** Reverse list **************************')
        reverse_list = [1, 3, 5, 100, 100]
        print(reverse_list)
        self._reverse_list(reverse_list)
        print(reverse_list)

        # p.254から


