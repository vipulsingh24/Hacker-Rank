'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
'''

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if ((s[-2:] == 'PM') and (int(s[:2])<12)):
        return (str(int(s[:2]) + 12)+s[2:-2])
    elif ((s[:2] == '12') and (s[-2:] == 'AM')):
        return ('00'+s[2:-2])
    elif ((s[-2:] == 'PM') and (int(s[:2]) == 12)):
        return (s[:-2])
    else:
        return (s[:-2])
        
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

