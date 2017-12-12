class Group:
    def __init__(self, name, students = []):
        self.name = name
        self._students = students

    def add_student(self, student):
        self._students.append(student)

    def get_students(self):
        return self._students

    def del_student(self, student):
        if student in self._students:
            self._students.pop(student)
            return self._students
        else:
            return 0

    def get_average_mark(self):
        average_mark = 0
        average_mark_exam = 0
        for student in self._students:
            average_for_student = sum(student.list_marks) / len(student.list_marks)
            average_mark_exam += student.exam_mark
            average_mark += average_for_student
        average_mark /= len(self._students)
        average_mark_exam /= len(self._students)
        return '=' * 60 + '\n' \
            'Средняя оценка за домашние задания по группе: {}\nСредняя оценка за экзамен: {} '\
            .format(average_mark, average_mark_exam)

    def get_average_by_sex(self):
        male_homework_average = 0
        female_homework_average = 0
        male_exam_average = 0
        female_exam_average = 0
        male_student = 0
        female_student = 0

        for student in self._students:
            if student.sex == 'male':
                male_homework_average += sum(student.list_marks) / len(student.list_marks)
                male_exam_average += student.exam_mark
                male_student += 1
            else:
                female_homework_average += sum(student.list_marks) / len(student.list_marks)
                female_exam_average += student.exam_mark
                female_student += 1

        male_homework_average /= male_student
        male_exam_average /= male_student
        female_exam_average /= female_student
        female_homework_average /= female_student

        return '=' * 60 + '\n' \
            'Средняя оценка за домашние задания у мужчин: {}\n\
Средняя оценка за экзамен у мужчин: {}\n\
Средняя оценка за домашние задания у женщин: {}\n\
Средняя оценка за экзамен у женщин: {}'\
            .format(male_homework_average, male_exam_average, female_homework_average, female_exam_average)

    def get_average_by_experience(self):
        withexp_homework_average = 0
        withexp_exam_average = 0
        withoutexp_homework_average = 0
        withoutexp_exam_average = 0
        withexp_student = 0
        withoutexp_student = 0

        for student in self._students:
            if student.past_experience == 1:
                withexp_homework_average += sum(student.list_marks) / len(student.list_marks)
                withexp_exam_average += student.exam_mark
                withexp_student += 1
            else:
                withoutexp_homework_average += sum(student.list_marks) / len(student.list_marks)
                withoutexp_exam_average += student.exam_mark
                withoutexp_student += 1

        withexp_homework_average /= withexp_student
        withexp_exam_average /= withexp_student
        withoutexp_exam_average /= withoutexp_student
        withoutexp_homework_average /= withoutexp_student

        return '=' * 60 + '\n' \
            'Средняя оценка за домашние задания у студентов с опытом: {}\n\
Средняя оценка за экзамен у студентов с опытом: {}\n\
Средняя оценка за домашние задания у студентов без опыта: {}\n\
Средняя оценка за экзамен у студентов без опыта: {}' \
            .format(withexp_homework_average, withexp_exam_average, withoutexp_homework_average, withoutexp_exam_average)

    def get_best_student(self):
        max_mark = 0
        best_students = []

        for student in self._students:
            if max_mark <= student.average_mark:
                max_mark = student.average_mark

        for student in self._students:
            if student.average_mark == max_mark:
                best_students.append(student)

        resoult_string = '=' * 60 + '\n'
        if len(best_students) > 1:
            resoult_string += 'Лучшие студенты: '
            for student in best_students:
                resoult_string += student.name + ' ' + student.surname + ', '
            resoult_string += 'с интегральной оценкой ' + str(max_mark)
        else:
            resoult_string += 'Лучший студет: {} {} с интегратной ценкой {}'\
                .format(best_students[0].name, best_students[0].surname, max_mark)

        return resoult_string

