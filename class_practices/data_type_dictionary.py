# Dictionary
"""Dictionary in Python is a collection of keys values,"""
"""Dictionary holds key:value pair. Key-Value is provided in the dictionary to make it more optimized."""

# declaring the
dict = {}
print("the given dict is {}".format(dict))

dict1 = {1:"abhi", 2:"mulbagal", 3:"Maruthi Nagar"}
print("this is one way to declare the Dictionary {}".format(dict1))

# length of dictionary and dict type

dict_len = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
dict_type = type(dict_len)
print(dict_type)
length = len(dict_len)
print("the length of the given dict is {}".format(length))
print("the given dict is {}".format(dict_len))

ind_dict = dict_len[3]
print("****the index is {}".format(ind_dict))


# Accessing by using index value
dict_ind = {'one':"name", 'two':"address", 'three':"pincode", 'four':"landmark"}
dict_val_one = dict_ind['one']
print("the dict value one is {}".format(dict_val_one))
dict_val_two = dict_ind['two']
print("the value of two is {}".format(dict_val_two))
dict_val_three = dict_ind['three']
print(" the value of three is {}".format(dict_val_three))
dict_val_four = dict_ind['four']
print("the value of four is {}".format(dict_val_four))

# adding elements to dictionary
dict_ind['seven'] = "hometown"
dict_ind['eight'] = 'state'
print("the value after adding the details is {}".format(dict_ind))

# Updating existing Key's Value
dict_ind['two'] = "last name"
dict_ind['three'] = "address"
dict_ind['four'] = "pincode"
dict_ind['seven'] = "landmark"
dict_ind['eight'] = "City"
print("the value after updating the key values is {}".format(dict_ind))

# using get() method
dict_get_one = dict_ind.get('one')
print("the value using the get method is {}".format(dict_get_one))

dict_get_two = dict_ind.get('four')
print("the value using the get method is {}".format(dict_get_two))

# items() method
dict_ind.items()
print("the items in the dictionary by using item method is {}".format(dict_ind))

# # keys() method
# dict_ind.keys()
# print("the keys in the dictionary are by using the keys method {}".format(dict_ind))
#
# dict_ind.pop()
# print("the elements after the pop is {}".format(dict_ind))
#
# dict_ind.update('abcdknd')
# print("the dict after update is {}".format(dict_ind))

dict_asg = {"name1":"python", "name2":"programming", 'name3':"concepts" }
print("the given dictionary is {}".format(dict_asg))


