from statistics import median
universities = [['Jamica Institute of Technology', 2175, 37704],['McJons', 19627, 39849],['Massachusetts Institute of Technology', 10566, 40732],['Princeton', 7802, 37000],['Garri', 5879, 35551],['Stanford', 19535, 40569],['Yale', 11701, 40500]]


student_enrollment = []
student_tuition = []
z = 0
while z < 7:
    a = universities[z][1]
    b = universities[z][2]
    student_enrollment.append(a)
    student_tuition.append(b)
    z += 1
def enrollment_stats():
    print(f'Student enrollment values are:\n{student_enrollment}')
    print(f'Student tuition fees are:\n{student_tuition}')
    
def mean(v):
    v = sum(v)/7
    print(v)
def median(v):
    pass

print(median(student_tuition))
