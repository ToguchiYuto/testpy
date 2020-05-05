'''
Created on 2020/05/05

@author: YutoToguchi
'''



print('My name is {} {}'.format('Yuto', 'Toguchi'))

a = 3
b = 8
# a = int(input('a:'))
# b = int(input('b:'))

a, b = sorted([a, b])

counter = a;
while counter <= b:
    print(counter, end=' ')
    counter += 1
print()

for i in range(5):
    print(i, end=' ')
print()

for _ in range(10):
    print('*', end=' ')
    break
else:
    print('else')
print()

for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')
print()

if a:
    print('in')

str = 'ABCDEFG'
for i, ch in enumerate(str):
    print('str[{}] = {}'.format(i, ch))

for i, ch in enumerate(str, 10):
    print('str[{}] = {}'.format(i, ch))

print('{:+} {:-} {: }'.format(77, 77, 77))
print('{:+} {:-} {: }'.format(-77, -77, -77))
print('{:b}'.format(1234567))
print(f'{1234567:b}')
print('{0:o} {0:#o}'.format(1234567))
print(f'{1234567:o} {1234567:#o}')
print('{0:x} {0:#x}'.format(1234567))
print(f'{1234567:x} {1234567:#x}')


def list_append(a, lst=[]):
    lst += a
    print(lst)


list_append([1])
list_append([2])
list_append([3, 4])


def print_digit(*num: tuple) -> list:

    """

    :param num:
    :return:
    """
    for i in range(len(num)):
        print(i, end=' ')
    print()


print_digit(1, 2, 3)
help(print_digit)
print(print_digit.__annotations__)
print(print_digit.__doc__)

tuple1 = (1, 3, 4, 2)
tuple2 = (1,)
print(tuple1)
print(type(tuple1))
print(type(tuple2))
div, mod = divmod(13, 3)
print('{} and {}'.format(div, mod))

for i in tuple1:
    print(i, end=' ')
print()

print(1 in tuple1)
print(tuple1[2])

list1 = list(tuple1)
print('id:{} type{}'.format(id(tuple1), type(tuple1)))
print('id:{} type{}'.format(id(list1), type(list1)))




if __name__ == '__main__':
    pass