from num2words import num2words

import math



def factorial_string(number):
    factorial = math.factorial(number)
    result = num2words(factorial)
    return result


def test_fact_num():
    number = factorial_string(1)
    assert number == "one"


def test_12_num():
    number = factorial_string(12)
    assert number == "four hundred and seventy-nine million, one thousand, six hundred"


def test_8_num():
    number = factorial_string(8)
    assert number == "forty thousand, three hundred and twenty"


def test_5_num():
    number = factorial_string(5)
    assert number == "one hundred and twenty"
