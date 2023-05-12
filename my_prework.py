"""
Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

The first line of the code has been defined as below.
"""

def hello_name(user_name):
    """
    Return a nice little hello message for the user.  
    """
    print("hello_" + user_name + "!")

"""
Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
"""

def first_odds():
    """
    Print odd numbers. There's no return for this one. 
    """
    for i in range(1, 101, 2):
        print(i)

"""
Question 3: 
Please write a Python function, max_num_in_list to return the max number of a given list. 

The first line of the code has been defined as below.
"""

def max_num_in_list(a_list):
    """
    Get the max of some list. 
    """
    if len(a_list) == 0:
        return None
    else:
        m = a_list[0]
        for n in a_list:
            if n > m:
                m = n
        return m
    
"""
Question 4:
Write a function to return if the given year is a leap year. 

A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
"""
    
def is_leap_year(a_year):
    """
    Is is a leap year? 
    """
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
"""
Question 5:
Write a function to check to see if all numbers in list are consecutive numbers. 

For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
"""
    
def is_consecutive(a_list):
    """
    For a given list a_list, check if the list of numbers is consecutive.
    """
    a_list = sorted(a_list) # Sort the list. 
    for i in range(len(a_list) - 1): # Begin with the penultimate list member. 
        if a_list[i+1] - a_list[i] != 1: # Check the difference between it and the previous list member. 
            return False # Is it consecutive? 
    return True

# Test cases
# print(is_consecutive([1,2,3]))
# print(is_consecutive([1,1,1]))
# print(is_consecutive([3,2,1]))

