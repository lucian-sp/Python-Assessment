from datetime import date

import pytest

from assignment2 import months_interval


def test_january_to_march():
    january = date(2017, 1, 1)
    march = date(2017, 3, 1)

    months = months_interval(january, march)

    assert(['January', 'February', 'March'] == months), months


def test_december_to_january():
    december = date(2017, 12, 1)
    january = date(2018, 1, 1)

    months = months_interval(december, january)

    assert(['January', 'December'] == months), months


def test_january_to_january():
    january2017 = date(2017, 1, 1)
    january2018 = date(2018, 1, 1)

    months = months_interval(january2017, january2018)

    assert(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'] == months), months
