from BigData_Podshivalova.hw6.tasks.task_hw6_oop_2 import Student, Teacher, HomeworkResult, DeadLineError, Homework
import datetime
import pytest

student= Student("Roman", "Petrov")
teacher = Teacher("Aleksandr", "Smetanin")
unlate_homework= Homework("text1", datetime.timedelta(days=3))
late_homework = Homework("text2", datetime.timedelta(days=-5))
homework_result_1 = HomeworkResult(student, late_homework, "str")
homework_result_2 = HomeworkResult(student, unlate_homework, "string")
homework_result_3 = HomeworkResult(student, late_homework, "solution")


def test_HomeworkResult():
    assert isinstance(homework_result_1, HomeworkResult)


def test_teacher_check_homework_1():
    assert not teacher.check_homework(homework_result_1)
    assert not teacher.check_homework(homework_result_2)
    assert teacher.check_homework(homework_result_3)


def test_teacher_homework_result_container():
    assert len(Teacher.homework_done) == 1


def test_teacher_reset_results_container():
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0