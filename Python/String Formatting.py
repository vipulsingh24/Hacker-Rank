def print_formatted(n):
    w = len('{:b}'.format(n))
    for i in range(1, n+1):
        print(str.rjust(str(i), w),\
              str.rjust('{:o}'.format(i), w),\
              str.rjust('{:X}'.format(i), w),\
              str.rjust('{:b}'.format(i), w))
