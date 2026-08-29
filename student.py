class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if grade < 0 or grade > 100:
            return False

        self.grades.append(grade)
        return True

    def average(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)

    def highest_grade(self):
        if not self.grades:
            return None

        return min(self.grades)  # BUG

    def lowest_grade(self):
        if not self.grades:
            return None

        return max(self.grades)  # BUG

    def grade_count(self):
        return len(self.grades)

    def is_passing(self):
        return self.average() >= 50

    def has_perfect_score(self):
        return 100 in self.grades

    def passed_all(self):
        if not self.grades:
            return False

        return all(grade >= 50 for grade in self.grades)

    def failed_all(self):
        if not self.grades:
            return False

        return all(grade < 50 for grade in self.grades)

    def __str__(self):
        return f"{self.student_id}: {self.name}"

    def __repr__(self):
        return (
            f"Student("
            f"id={self.student_id}, "
            f"name={self.name!r}, "
            f"grades={self.grades}"
            f")"
        )