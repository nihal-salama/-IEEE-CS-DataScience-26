students_num = int(input())
students = []

for i in range(students_num):
    stu_data = []
    student = input().capitalize()
    grade = float(input())
    stu_data.insert(0,student)
    stu_data.insert(1,grade)
    students.append(stu_data)

grades = []
for i in range(students_num):
    grades.append(students[i][1])
    grades.sort()

for i in range(students_num):
    if grades[i] > grades[0]:
        sec_low = grades[i]
        break

sec_low_list = []
for i in range(students_num):
    if students[i][1] == sec_low:
        sec_low_list.append(students[i][0])

sec_low_list.sort()
for i in sec_low_list:
    print(i)
