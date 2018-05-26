'''
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.


Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
'''

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    grade_5 = []
    for i in grades:
        grade_5.append(i + (5 - (i %5)))
    
    for i in range(len(grade_5)):
        if grade_5[i] < 38:
            grade_5[i] = grades[i]
        elif (grade_5[i] - grades[i] < 3):
            grade_5[i] = grade_5[i]
        else:
            grade_5[i] = grades[i]
    return grade_5

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

