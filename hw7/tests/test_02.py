from hw7.homework7.task_02 import backspace_compare
import pytest


@pytest.mark.parametrize(('line1', 'line2'), (('la#if#ne', 'll#ineo#'),
                                               ('##mo#omghj###', '##mhg##omlkj###i#')))
def test_backspace_compare_positive(line1, line2):
    assert backspace_compare(line1, line2)


@pytest.mark.parametrize(('line1', 'line2'), (('la#if#ne', 'llh#inefeo#'),
                                               ('##jhmo#omghj###', '##mhhig##omlkj##g#i#')))
def test_backspace_compare_positive(line1, line2):
    assert not backspace_compare(line1, line2)
    