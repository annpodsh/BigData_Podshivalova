from hw5.tasks.task_hw5_oop_1 import Homework, Student, Teacher
import datetime


# checking the health of creating a Homework class element

def test_homework():
    hw = Homework("solve the linear equation", datetime.timedelta(1))
    assert hw.text == "solve the linear equation"
    hw = Homework("solve the differential equation", datetime.timedelta(-1))
    assert hw.text == "solve the differential equation"


# checking the functionality of the function that checks the status of the task relative to the deadline:
# there is time before the deadline

def succes_test_homework():
    hw = Homework("solve the linear equation", datetime.timedelta(1))
    assert hw.is_active()


# health check of the function that checks the status of the task relative to the deadline: the deadline has passed

def unsucces_test_homework():
    hw = Homework("solve the differential equation", datetime.timedelta(-1))
    assert not hw.is_active()


# checking the health of creating a Student class element

def test_student():
    student = Student("Petrov", "Leonid")
    assert student.first_name == "Petrov"
    assert student.last_name == "Leonid"


# checking the functionality of the function that checks the success of the task: managed in time

def test_student_homework_in_time(capsys):
    student = Student("Petrov", "Leonid")
    hw = Homework("solve the linear equation", datetime.timedelta(1))
    do_homework=stud.do_homework(hw)
    assert do_homework == hw


# checking the functionality of the function that checks the success of the task: did not have time in time

def test_student_homework_late(capsys):
    student = Student("Petrov", "Leonid")
    hw = Homework("solve the differential equation", datetime.timedelta(-1))
    do_homework = stud.do_homework(hw)
    assert do_homework == hw


# checking the health of creating a Teacher class element

def test_teacher():
    teacher = Teacher("Vlasova", "Zoye")
    assert teacher.first_name == "Vlasova"
    assert teacher.last_name == "Zoye"


# checking the functionality of the function that determines the text of the task and the deadline

def test_teacher_homework_create():
    teacher = Teacher("Vlasova", "Zoye")
    hw=teacher.create_homework("solve the linear equation", 5)
    assert hw.is_active()
    assert hw.text == "solve the linear equation"