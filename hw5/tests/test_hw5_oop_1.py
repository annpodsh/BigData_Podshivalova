from BigData_Podshivalova.hw5.tasks.task_hw5_oop_1 import Homework, Student, Teacher
import datetime


# checking the health of creating a Homework class element

hw1 = Homework("solve the linear equation", datetime.timedelta(1))
hw2 = Homework("solve the differential equation", datetime.timedelta(-1))
student = Student("Petrov", "Leonid")
teacher = Teacher("Vlasova", "Zoye")


def test_homework():
    assert hw1.text == "solve the linear equation"
    assert hw2.text == "solve the differential equation"


# checking the functionality of the function that checks the status of the task relative to the deadline:
# there is time before the deadline

def succes_test_homework():
    assert hw1.is_active()


# health check of the function that checks the status of the task relative to the deadline: the deadline has passed

def unsucces_test_homework():
    assert not hw2.is_active()


# checking the health of creating a Student class element

def test_student():
    assert student.first_name == "Petrov"
    assert student.last_name == "Leonid"


# checking the functionality of the function that checks the success of the task: managed in time

def test_student_homework_in_time():
    do_homework = stud.do_homework(hw1)
    assert do_homework == hw1


# checking the functionality of the function that checks the success of the task: did not have time in time

def test_student_homework_late():
    do_homework = stud.do_homework(hw2)
    assert do_homework == hw2


# checking the health of creating a Teacher class element

def test_teacher():
    assert teacher.first_name == "Vlasova"
    assert teacher.last_name == "Zoye"


# checking the functionality of the function that determines the text of the task and the deadline

def test_teacher_homework_create():
    hw_new = teacher.create_homework("solve the linear equation", 5)
    assert hw_new.is_active()
    assert hw_new.text == "solve the linear equation"
