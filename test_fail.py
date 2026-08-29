import pytest

from student import Student
from gradebook import GradeBook


# =========================
# STUDENT TESTS
# =========================

def test_student_creation():
    student = Student(1, "Alice")

    assert student.student_id == 1
    assert student.name == "Alice"
    assert student.grades == []


def test_add_grade():
    student = Student(1, "Alice")

    assert student.add_grade(80) is True
    assert student.grades == [80]


def test_invalid_grade():
    student = Student(1, "Alice")

    assert student.add_grade(101) is False
    assert student.add_grade(-1) is False
    assert student.grades == []


def test_student_average():
    student = Student(1, "Alice")

    student.add_grade(80)
    student.add_grade(90)
    student.add_grade(70)

    assert student.average() == 80


def test_student_highest_grade():
    student = Student(1, "Alice")

    student.add_grade(60)
    student.add_grade(90)
    student.add_grade(75)

    assert student.highest_grade() == 90


def test_student_lowest_grade():
    student = Student(1, "Alice")

    student.add_grade(60)
    student.add_grade(90)
    student.add_grade(75)

    assert student.lowest_grade() == 60


def test_empty_average():
    student = Student(1, "Alice")

    assert student.average() == 0


def test_grade_count():
    student = Student(1, "Alice")

    student.add_grade(80)
    student.add_grade(90)

    assert student.grade_count() == 2


def test_is_passing():
    student = Student(1, "Alice")

    student.add_grade(60)
    student.add_grade(70)

    assert student.is_passing() is True


def test_is_failing():
    student = Student(1, "Alice")

    student.add_grade(30)
    student.add_grade(40)

    assert student.is_passing() is False


def test_perfect_score():
    student = Student(1, "Alice")

    student.add_grade(80)
    student.add_grade(100)

    assert student.has_perfect_score() is True


def test_passed_all():
    student = Student(1, "Alice")

    student.add_grade(60)
    student.add_grade(70)
    student.add_grade(80)

    assert student.passed_all() is True


# =========================
# GRADEBOOK TESTS
# =========================

def test_add_student():
    book = GradeBook()

    student = Student(1, "Alice")

    assert book.add_student(student) is True
    assert book.get_student(1) == student


def test_duplicate_student():
    book = GradeBook()

    student = Student(1, "Alice")

    assert book.add_student(student) is True
    assert book.add_student(student) is False


def test_remove_student():
    book = GradeBook()

    student = Student(1, "Alice")

    book.add_student(student)

    assert book.remove_student(1) is True
    assert book.get_student(1) is None


def test_student_count():
    book = GradeBook()

    book.add_student(Student(1, "Alice"))
    book.add_student(Student(2, "Bob"))
    book.add_student(Student(3, "Charlie"))

    assert book.get_student_count() == 3


def test_add_grade_to_student():
    book = GradeBook()

    book.add_student(Student(1, "Alice"))

    assert book.add_grade(1, 85) is True
    assert book.get_student(1).grades == [85]


def test_add_grade_to_unknown_student():
    book = GradeBook()

    assert book.add_grade(999, 80) is False


def test_gradebook_average():
    book = GradeBook()

    book.add_student(Student(1, "Alice"))

    book.add_grade(1, 80)
    book.add_grade(1, 100)

    assert book.get_average(1) == 90


def test_gradebook_highest_grade():
    book = GradeBook()

    book.add_student(Student(1, "Alice"))

    book.add_grade(1, 60)
    book.add_grade(1, 95)
    book.add_grade(1, 75)

    assert book.get_highest_grade(1) == 95


def test_gradebook_lowest_grade():
    book = GradeBook()

    book.add_student(Student(1, "Alice"))

    book.add_grade(1, 60)
    book.add_grade(1, 95)
    book.add_grade(1, 75)

    assert book.get_lowest_grade(1) == 60


def test_grade_count_from_book():
    book = GradeBook()

    book.add_student(Student(1, "Alice"))

    book.add_grade(1, 50)
    book.add_grade(1, 60)
    book.add_grade(1, 70)

    assert book.get_grade_count(1) == 3


def test_class_average():
    book = GradeBook()

    alice = Student(1, "Alice")
    bob = Student(2, "Bob")

    book.add_student(alice)
    book.add_student(bob)

    book.add_grade(1, 80)
    book.add_grade(1, 100)

    book.add_grade(2, 60)
    book.add_grade(2, 80)

    assert book.get_class_average() == 80


def test_top_student():
    book = GradeBook()

    alice = Student(1, "Alice")
    bob = Student(2, "Bob")

    book.add_student(alice)
    book.add_student(bob)

    book.add_grade(1, 70)
    book.add_grade(1, 80)

    book.add_grade(2, 90)
    book.add_grade(2, 100)

    assert book.get_top_student().name == "Bob"


def test_failing_students():
    book = GradeBook()

    alice = Student(1, "Alice")
    bob = Student(2, "Bob")

    book.add_student(alice)
    book.add_student(bob)

    book.add_grade(1, 30)
    book.add_grade(1, 40)

    book.add_grade(2, 80)
    book.add_grade(2, 90)

    failing = book.get_failing_students()

    assert len(failing) == 1
    assert failing[0].name == "Alice"


def test_empty_gradebook_average():
    book = GradeBook()

    assert book.get_class_average() == 0