import unittest
from unittest import mock
from monify import Monify
import builtins


#from functools import  wraps


class MyTestCase(unittest.TestCase):
    def test_add_income(monkeypatch):
        monkeypatch.__setattr__('builtins.input', lambda _: "2020-11-10")
        monkeypatch.__setattr__('builtins.input', lambda _: "10000")


    # go about using input() like you normally would:
    income_date = input("'Enter Date (YYYY-MM-DD)\n: -->")
    income = int(input("Enter your income for the month \n: --> "))
    assert income_date == "2020-11-10"
    assert income == 10000

    def test_expenditure(monkeypatch):
        Monify.add_expenditure.input = lambda: 'some_other_input'
        output = Monify.add_expenditure
        assert output == 'another_expected_output'



if __name__ == '__main__':
    unittest.main ()
