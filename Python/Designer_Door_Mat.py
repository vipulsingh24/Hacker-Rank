'''
Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
'''

def door_mat(n,m):
    for i in range(1,n,2):
        print(('.|.'*(i)).center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for i in reversed(range(1,n,2)):
        print(('.|.'*(i)).center(m, '-'))

n, m = [int(x) for x in input().split()]
door_mat(n, m)
