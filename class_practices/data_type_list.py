# the list concepts

"""The list is collection of elements it contains alphabets, numbers and alphanumeric
or combinations of all which is represented between square braces. """

# List is mutable


# declering the empty list+999999

emp_lst = []
print(emp_lst)

empty_lst = list()
print(empty_lst)

lst=[10, "abhi", "mbl", "20", "bangalore"]
print(lst)

type_list = type(lst)
print("the type of the give list is {}".format(type_list))

#Reverse indexing
str = "python"
frst_neg_str = str[-1]
print("The value of first negative index of string is {}".format(frst_neg_str))
scnd_neg_str = str[-2]
print("The value of second negative index of string is {}".format(scnd_neg_str))
thrd_neg_str = str[-3]
print("The value of third negative index of string is {}".format(thrd_neg_str))
frth_neg_str = str[-4]
print("The value of fourth negative index of string is {}".format(frth_neg_str))
fif_neg_str = str[-5]
print("The value of fifth negative index of string is {}".format(fif_neg_str))
six_neg_str = str[-6]
print("The value of sixth negative index of string is {}".format(six_neg_str))


# Slicing
str_zer_to_sec_ind = str[0:3]
print("The value of slicing from zero to second index of a string is {}".format(str_zer_to_sec_ind))
str_two_to_fifth = str[2:6]
print("The value of slicing from second to fifth index of a string is {}".format(str_two_to_fifth))
str_four_to_five = str[4:6]
print("The value of slicing from fourth to fifth index of string is {}".format(str_four_to_five))
