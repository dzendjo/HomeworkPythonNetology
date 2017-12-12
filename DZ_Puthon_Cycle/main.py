import student
import group

student1 = student.Student('Vasia', 'Petrov', 'male', 1, [6, 7, 8, 8, 7], 8)
student2 = student.Student('Anton', 'Zheleznyak', 'male', 1, [8, 7, 7, 5, 8], 7)
student3 = student.Student('Vika', 'Antonova', 'female', 0, [6, 5, 7, 6, 7], 7)
student4 = student.Student('Felix', 'Edmubdovich', 'male', 0, [7, 5, 6, 4, 6], 6)
student5 = student.Student('Antonina', 'Nikitina', 'female', 0, [9, 8, 9, 9, 10], 9)
student6 = student.Student('Maksim', 'Zheleznyak', 'male', 1, [8, 9, 9, 10, 9], 9)

group = group.Group('1112D', [student1, student2, student3, student4, student5, student6])

print(group.get_average_mark())
print(group.get_average_by_sex())
print(group.get_average_by_experience())
print(group.get_best_student())