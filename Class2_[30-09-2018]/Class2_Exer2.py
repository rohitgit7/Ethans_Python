student_list = []
first_name = []

student1 = raw_input("Enter student full name, age, class:\n")
student1 = student1.split(' ')
student_list.append(student1)
first_name.append(student1[0])

student2 = raw_input("Enter student full name, age, class:\n")
student2 = student2.split(' ')
student_list.append(student2)
first_name.append(student2[0])

student3 = raw_input("Enter student full name, age, class:\n")
student3 = student3.split(' ')
student_list.append(student3)
first_name.append(student3[0])

print student_list
print "Total no. of students are:",len(student_list)

Total_Age = int(student_list[0][2]) + int(student_list[1][2]) + int(student_list[2][2])
print "Sum of all ages is:",Total_Age

print "All first names in capital letters:",student_list[0][0].upper() + "," + student_list[1][0].upper()

first_name.sort()
print "first names in sorted order:",first_name

print "last name in reverse word:",student_list[0][1][::-1], student_list[1][1][::-1], student_list[2][1][::-1]

