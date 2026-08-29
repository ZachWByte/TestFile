from student import Student


class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            return False

        self.students[student.student_id] = student
        return True

    def get_student(self, student_id):
        return self.students.get(student_id)

    def remove_student(self, student_id):
        if student_id not in self.students:
            return False

        del self.students[student_id]
        return True

    def add_grade(self, student_id, grade):
        student = self.get_student(student_id)

        if student is None:
            return False

        if grade < 0 or grade > 100:
            return False

        student.grades.append(grade)
        return True

    def get_average(self, student_id):
        student = self.get_student(student_id)

        if student is None or not student.grades:
            return 0

        return sum(student.grades) / len(student.grades)

    def get_highest_grade(self, student_id):
        student = self.get_student(student_id)

        if student is None or not student.grades:
            return None

        return min(student.grades)  # BUG

    def get_lowest_grade(self, student_id):
        student = self.get_student(student_id)

        if student is None or not student.grades:
            return None

        return max(student.grades)  # BUG

    def get_passing(self, student_id):
        student = self.get_student(student_id)

        if student is None:
            return False

        return self.get_average(student_id) >= 50

    def get_grade_count(self, student_id):
        student = self.get_student(student_id)

        if student is None:
            return 0

        return len(student.grades)

    def get_student_count(self):
        return len(self.students)

    def get_all_students(self):
        return list(self.students.values())

    def get_class_average(self):
        if not self.students:
            return 0

        averages = []

        for student in self.students.values():
            if student.grades:
                averages.append(sum(student.grades) / len(student.grades))

        if not averages:
            return 0

        return sum(averages) / len(averages)

    def get_top_student(self):
        if not self.students:
            return None

        students_with_grades = [
            student
            for student in self.students.values()
            if student.grades
        ]

        if not students_with_grades:
            return None

        return max(
            students_with_grades,
            key=lambda student: sum(student.grades) / len(student.grades)
        )

    def get_failing_students(self):
        return [
            student
            for student in self.students.values()
            if student.grades
            and sum(student.grades) / len(student.grades) < 50
        ]