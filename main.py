#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
first_name
"""first _name is valid because, it starts with a lowercase and uses an underscore"""
2nd_name
"""2nd_name is invalid because, it starts with a number"""
age
"""age is valid because, it starts with a lowercase and it is letters only """
total_amount
"""total_amount is valid because, it starts with a lowercase and there is an underscore"""
while
"""while is valid because, it starts with a lowercase and uses letters only """
Student
"""Student is invalid because, it starts with a capital"""
my-variable
"""my-variable is invalid because, it uses a -"""
for
"""for is valid because, it starts with a lowercase and it uses letters only """
_temp
"""_temp is valid because, it starts with a underscore"""
value#
"""value# is invalid because, # are not allowed """

"""
# Problem 2
"""
calculate_total
"""calculate_total is valid because, starts with lowercase and also uses a underscore """
3rd_function
"""3rd_function is invalid because, it starts with a number"""
print_values
"""print_values is valid because, it starts with lowercase and also uses a underscore """
find-item
"""find-item is invalid because, it uses a -"""
def
"""def is valid because, it starts with a lowercase and also it is only letters"""
updateProfile
"""updateProfile is valid because. It starts with a lowercase and uses a capital to merge the two words instead of a space or -"""
my_function
"""my_function is valid because, it starts with a lowercase and also uses a underscore"""
try
"""try is valid because, it starts with a lowercase and also uses only letters"""
init_data
"""init_data is valid because, it starts with a lowercase and also uses a underscore"""
value@function
"""value@function  is invalid because, there is a @ in the function name """

"""
# Problem 3
"""
True and False
"""True and False is valid, because it is a boolean"""
5 > 3 or "apple" < "banana"
"""5 > 3 or "apple" < "banana" is valid because,5 is greater than 3 and apple comes before banana"""
not 10 <= 20
("""not 10 <= 20 is valid because, 20 is greater and more than equal to 10"""
True or 5 = 4
("""True or 5 = 4 is invalid because, 5 does not equal to 4"""
"apple" != "orange" and 5
(""" “apple” != “orange” and 5 ????"""
3 < 5 not True
("""3 < 5 not True is valid because, 3 is not greater than 5"""
False == (3 > 4)
("""False == (3 > 4) is valid because, 4 is greater than 3"""
10 <= "10"
("""10 <= “10” is invalid because of <=”10”? What does this even mean?"""
True or not False
("""True or not False is valid because, true is true. If something isn't false its true."""
5 and or 4
("""5 and or 4 is not valid because, what is being compared?"""

"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
