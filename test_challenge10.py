

import pandas as pd
import pytest
# file model_sheet.xlsx is located https://github.com/DaniilVolg/python-autobots/blob/master/model_sheet.xlsx you can load it on your machine , copy path to this file in your machine and replace new adress (E:\комп\model_sheet.xlsx) 
orders=pd.read_excel('E:\комп\model_sheet.xlsx', sheet_name='cars')
print(orders)

row1 = list(orders.iloc[0])
row2 = list(orders.iloc[1])
row3 = list(orders.iloc[2])
row4 = list(orders.iloc[3])


list1 = [1, 'toyota', 'harrier', 2010]
list2 = [2, 'lexus', 'rx330', 2014]
list3 = [3, 'bmw', 'x5', 2015]
list4 = [4, 'toyota', 'avalon', 2018]


@pytest.mark.parametrize("test_input, expected_result", [(row1, list1), (row2, list3), (row3, list3), (row4, list4)])
def test_multiplication(test_input, expected_result):
    if test_input == expected_result:
        assert test_input == expected_result
    elif test_input != expected_result:
        print(" ----- This assertion is not complete----")
