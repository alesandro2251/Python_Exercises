# Create a program that calculates bonus points for each student enrolled in a course. On the first line,
# you are going to receive the number of students. On the second line, you will receive the total number of lectures
# in the course. The course has an additional bonus, which you will receive on the third line. On the following
# lines, you will be receiving the count of attendances for each student.

import math

studentsNumber = int(input())
lectures = int(input())
additionalBonus = int(input())
maxPoints = 0
attend = 0

for i in range(studentsNumber):
    studentAttendance = int(input())
    if lectures == 0:
        totalBonus = 0
    else:
        totalBonus = studentAttendance / lectures * (5 + additionalBonus)
    if totalBonus > maxPoints:
        maxPoints = totalBonus
        attend = studentAttendance

print(f"Max Bonus: {math.ceil(maxPoints)}.")
print(f"The student has attended {attend} lectures.")
