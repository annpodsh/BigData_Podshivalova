"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Ученик, учитель, Домашнее задание)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
 homework - для объекта Homework, если передан не этот класс - выкинуть
 подходящие по смыслу исключение с сообщением:
 "Вы дали не домашнее задание"

 solution - хранит решение ДЗ как строку
 author - хранит объект Student
 created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Учительница
Атрибут:
 homework_done - структура с интерфейсом как в словаря, сюда поподают все
 HomeworkResult после успешного прохождения check_homework
 (нужно гаранитровать остутствие повторяющихся результатов по каждому
 заданию), группировать по экземплярам Homework.
 Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
 check_homework - принимает экземпляр HomeworkResult и возвращает True если
 ответ студента больше 5 символов, так же при успешной проверке добавить в
 homework_done.
 Если меньше 5 символов - никуда не добавлять и вернуть False.

 reset_results - если передать экземпряр Homework - удаляет только
 результаты этого задания из homework_done, если ничего не передавать,
 то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

import datetime
from collections import defaultdict


class Human:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


"""
Homework class, accept text of the task and time deadline attributes,
and have is_active() method, that returns boolean, if the task execution time has expired.
"""


class Homework:
    def __init__(self, text: str, deadline: datetime.timedelta):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        data = self.created + self.deadline
        return self.created <= data


"""
The Homework Result class accepts the task author object, accepts the original task
and its solution as a string
"""


class HomeworkResult:
    def __init__(self, author: Student, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.homework = homework
        self.author = author
        self.solution = solution
        self.created = datetime.datetime.now()


"""
The Dead line Error class throws an exception when do_homework
"""


class DeadLineError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


"""
Student class, accept last_name and first_name attributes,
and have create_homework() method,
that takes task text and integer number of days left for doing this homework, and returns Homework instance
that contains task text and timedelta instance with days left
"""


class Student(Human):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)

    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadLineError("You are late")


"""
Teacher class, accept last_name and first_name attributes,
and have methods: 
create_homework, that the text of the task and the number of days for this task,
returns an instance of Homework
check_homework, that checks the length of the homework and, upon successful verification, adds to
homework_done
reset_results , that deletes only the results of this task from homework_done or completely resets homework_done
"""


class Teacher(Human):
    homework_done = defaultdict(lambda: [])

    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)

    def create_homework(self, task: str, days_left: int) -> Homework:
        return Homework(task, datetime.timedelta(days_left))

    def check_homework(self, homework_result: HomeworkResult) -> bool:
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework.text].append(homework_result)
            return True
        else:
            return False

    def reset_results(self, homework: Homework):
        Teacher.homework_done.pop(homework.text)


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
