#Print letter S using function :
'''
*******
*
*
*******
      *
      *
*******
'''


def print_s(n):
    for i in range(n):
        if i == 0 or i == n // 2 or i == n - 1:
            print('*' * n)
        elif i < n // 2:
            print('*')
        else:
            print(' ' * (n - 1) + '*')

print_s(7)
