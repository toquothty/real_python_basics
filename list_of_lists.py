# This space is just for review and challenge exercises.
#
# Perform cals on user input

import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19267, 39849],
    ['Massachusetts Instititue of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yales', 11701, 40500]
]

def enrollment_stats(list_universities):

    student_enrollment = []
    tuition_fees = []

    for university in list_universities:
        student_enrollment.append(university[1])
        tuition_fees.append(university[2])
    
    return student_enrollment, tuition_fees

def mean(values):
    return sum(values) / len(values)

def median(values):
    return statistics.median(values)

total = enrollment_stats(universities)

print('************************************************')
print(f"Total Students:   {sum(total[0])}")
print(f"Total Tuition:   ${sum(total[1])} \n")
print(f"Student Mean:     {mean(total[0]):,.0f}")
print(f"Student Median:   {median(total[0])} \n")
print(f"Tuition Mean:   ${mean(total[1]):,.2f}")
print(f"Tution Median:  ${median(total[0])}")
print('**********************************************')