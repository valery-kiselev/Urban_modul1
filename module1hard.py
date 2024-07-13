grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
students_dict = dict(zip(students_list, grades))
average_score = {}
for key in students_dict:
    average_score.update({key: sum(students_dict[key])/len(students_dict[key])})
print(average_score)
