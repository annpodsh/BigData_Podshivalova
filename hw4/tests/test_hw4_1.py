import hw4.tasks.task_hw4_1
import pytest

'''
The built-in decorator pytest.mark.parametrize allows you to parameterize arguments: 
"keywords" is the keyword for the search, 
"S_data" is the source dataset, 
"expected_value" is the expected value
'''

@pytest.mark.parametrize(
 ["keywords", "S_data", "expected_value"],
    [
        ({"keyword1": "result1"}, [{"keyword1": "result1"}, {"keyword2": "result2"}], [{"keyword1": "result1"}])
    ]
)
#call function "Filter"
def test_make_filter(keywords, S_data, expected_value):
    assert hw4.tasks.task_hw4_1.make_filter(**keywords).apply(S_data) == expected_value