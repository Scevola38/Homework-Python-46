from database import StudentTable

connection_string = "postgresql://postgres:Margerit38@localhost:5432/postgres"
db = StudentTable(connection_string)


def test_add_student():
    # Тестирование добавления студента
    db.add_student(user_id=1, subject_id=2, level="Beginner",
                   education_form="full-time")
    students = db.get_students()
    assert len(students) > 0


def test_delete_student():
    # Тестирование удаления студента
    db.add_student(user_id=2, subject_id=3, level="Pre-Intermediate",
                   education_form="part-time")
    db.delete_student(user_id=2)
    students = db.get_students()
    assert all(student.user_id != 2 for student in students)


def test_get_students():
    # Тестирование получения студентов
    db.add_student(user_id=3, subject_id=4, level="Advanced",
                   education_form="full-time")
    students = db.get_students()
    assert any(student.user_id == 3 for student in students)


def test_delete_student_2():
    db.add_student(user_id=3, subject_id=2, level="Beginner",
                   education_form="full-time")
    db.delete_student(user_id=3)
    students = db.get_students()
    assert all(student.user_id != 3 for student in students)


def test_delete_student_3():
    db.add_student(user_id=1, subject_id=3, level="Pre-Intermediate",
                   education_form="part-time")
    db.delete_student(user_id=1)
    students = db.get_students()
    assert all(student.user_id != 1 for student in students)
