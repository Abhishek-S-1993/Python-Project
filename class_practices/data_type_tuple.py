"""
what is tuple?
tuple is a group of elements which can be alphabets, numbers and alphanumeric or combinations of all which
is represented between small braces.
*** tuple is immutable
"""

"""
Difference between list and tuple
List                                    Tuple

1. List is mutable                      1. Tuple is immutable
2. List can be appended and extended    2. Tuple cannot be appended or extended
3. List is slow                         3. Tuple is fast
4. List  allocates extra memory space   4. Tuple allocates memory space only for the declared elements
"""

"""
Why list is slow then tuple?
during run time it checks for all the memory space allocated for list where list has extra memory space, 
hence list is slow and tuple does not have extra memory space allocate
hence tuple is fast.
"""

# One way of declaring empty tuple

emp_t_tup = ()
print("The value of empty tuple is {}".format(emp_t_tup))

emp_tp = tuple()
print("The another way of creating empty tuple is {}".format(emp_tp))

tpl = (1, "a", "python@3")
print("The value of tuple is {}".format(tpl))

type_tpl = type(tpl)
print("the of tuple is {}".format(type_tpl))

tpl_one = (2,5,6,7,8,9)
tuple_len = len(tpl_one)
print("the length of the given tuple is {}".format(tuple_len))

tuple_num = (5,6, 88, 55, 45, 99, 22 ,56)
tpl_max = max(tuple_num)
print("the max value in the given tuple is {}".format(tpl_max))
tpl_min =  min(tuple_num)
print("the min value of the given tuple is {}".format(tpl_min))

# converting to tuple to list
tup = (1,2,3,4,5,6,7)
tup_lst = list(tup)
tup_type = type(tup_lst)
print(tup_type)

# converting tuple to String

tup_str = (1,2,3,4,5,6,)
str_con = str(tup_str)
str_type = type(str_con)
print(str_type)



