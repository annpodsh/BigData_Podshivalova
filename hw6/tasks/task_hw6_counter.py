"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


"""
created the Counting_Class class, 
the number of instances of which will be counted in the get_created_instance method, 
and the reset_instances_counter method will reset the counter."""


def instances_counter(cls):
    class Counting_Class(cls):
        i = 0

        def __init__(self):
            super().__init__()
            Counting_Class.i += 1

        @classmethod
        def get_created_instances(cls) -> int:
            return Counting_Class.i

        @classmethod
        def reset_instances_counter(cls) -> int:
            quantity = Counting_Class.i
            Counting_Class.i = 0
            return quantity

    return Counting_Class


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
