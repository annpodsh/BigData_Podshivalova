import hw4.tasks.task_hw4_3

#checking for data in the standard error descriptor

def test_my_precious_logger():
    assert hw4.tasks.task_hw4_3.my_precious_logger("error") == "OK"
