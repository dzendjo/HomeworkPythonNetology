class Student:
    def __init__(self, name, surname, sex, past_experience, list_marks, exam_mark):
        self.past_experience = past_experience
        self.sex = sex
        self.list_marks = list_marks
        self.exam_mark = exam_mark
        self.surname = surname
        self.name = name
        self.average_mark = 0.6 * (sum(self.list_marks) / len(self.list_marks)) + 0.4 * self.exam_mark