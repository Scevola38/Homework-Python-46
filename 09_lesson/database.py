from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    user_id = Column(Integer, primary_key=True)
    subject_id = Column(Integer)
    level = Column(String)
    education_form = Column(String)


class StudentTable:
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.__db)
        Base.metadata.create_all(self.__db)

    def add_student(self, user_id, subject_id, level, education_form):
        # Проверка на допустимые значения subject_id
        valid_subject_ids = [2, 3, 4]
        if subject_id not in valid_subject_ids:
            raise ValueError(f"Invalid subject_id: "
                             f"{subject_id}. Must be one of "
                             f"{valid_subject_ids}.")

        # Проверка на допустимые значения level
        valid_levels = \
            ["Beginner", "Pre-Intermediate", "Upper-Intermediate",
             "Advanced", "Elementary"]
        if level not in valid_levels:
            raise ValueError(f"Invalid level: {level}. "
                             f"Must be one of {valid_levels}.")

        session = self.Session()
        new_student = Student(user_id=user_id, subject_id=subject_id,
                              level=level, education_form=education_form)
        session.add(new_student)
        session.commit()
        session.close()

    def get_students(self):
        session = self.Session()
        students = session.query(Student).all()
        session.close()
        return students

    def delete_student(self, user_id):
        session = self.Session()
        try:
            student_to_delete = (
                session.query(Student).
                filter(Student.user_id == user_id).one_or_none())
            if student_to_delete:
                session.delete(student_to_delete)
                session.commit()
            else:
                raise ValueError(f"No student found with user_id: {user_id}")
        except Exception as e:
            session.rollback()  # Откат транзакции в случае ошибки
            raise e  # Повторно вызвать исключение
        finally:
            session.close()
