# # practice zone
# # a=10
# # b=20
# # print(a)
# # print(b)
# # print(a+b)
#
# print(" the", "pyhton", "programming", "is", "easy", sep = "-")
#
# # a = int(input("Enter the value of a : "))
# # print("the given value is : {}".format(a))
#
# # x= 20
# # x+=3
# # print(x)
#

# lst = (10, 20, 30, 40, 50)
# lst_rev = lst[1]
# print("the reverse list is {}".format(lst_rev))
# print("the given list is {}".format(lst))
# print("the given list type is{}".format(type(lst)))

str = "python class"
type_str = type(str)
print("the given string is {}".format(str))
print("the given string is of the type is {}".format(type_str))

#indexing
str_ind = str[1]
print("the index value of 1 is {}".format(str_ind))
str_ind_sec = str[2]
print("the index value of 2 is {}".format(str_ind_sec))
str_ind_three = str[3]
print("the index value of 3 is {}".format(str_ind_three))

#Reveser indexing
str_x = "the python class"
str_rev_one = str_x[-4]
print("the reverse indexing of the give number is {} ".format(str_rev_one))

str_y = "the python class"
str_rev_two = str_x[-10]
print("the reverse indexing of the give number is {} ".format(str_rev_two))

#The String Slicing

str_slicing_one = str[2:5]
print("the slicing of 2 is 5 is {}".format(str_slicing_one))

str_slicing_sec = str[0:5]
print("the slicing of 0 to 5 is {}".format(str_slicing_sec))

str_slicing_three = str[1:7]
print("the slicing of 1 to 7 is {}".format(str_slicing_three))

#string Capitailze

str_cap_one = "this is python session"
print("the value of given string after capitalize is {}".format(str_cap_one.capitalize()))

str_cap_two = "python programming is easy"
print("the given string is after capitalization is {}".format(str_cap_two.capitalize()))

# String Startingwith
str_start_one = "the start of python session"
print("the starting with method for the given text is {}".format(str_start_one.startswith("t")))

str_start_two = "the start of python session"
print("the starting with method for the given text is {}".format(str_start_two.startswith("p")))

# String Endswith
str_end_one = "the closure of python session"
print("the ends with method for the given text is {}".format(str_end_one.endswith("n")))

str_end_two = " the closure of python session"
print("the ends method with the give text is {}".format(str_end_two.endswith("e")))

# finding of the string
str_find_one = "the python session is useful"
print("the position of the given string is {}".format(str_find_one.find("s")))

str_find_two = "the python session will happen at night"
print("the position of the given string is {}".format(str_find_two.find("w")))

# String count
str_count_one = "the python elements counts"
print("the count of the given element is {}".format(str_count_one.count("e")))

str_count_two = "the python elements counts"
print("the count of the given element is {}".format(str_count_two.count("o")))

# String Replace
str_sen = "basket contains an APPLE, BANANA and ORANGE"
print("the given string is {}".format(str_sen))
str_rep = str_sen.replace("BANANA", "JACKFRUIT")
print("the string after replace has done {}".format(str_rep))

# string lower
str_low = "The Python Class WIll start in a while"
str_lower = str_low.lower()
print(str_lower)

# string higher
str_hig = "The Python Class WIll start in a while"
str_higher = str_low.upper()
print(str_higher)

# check isalpha, isnumeric, isupper, islower, isalnum, isdecimal
str_one = "python"
str_two = "123"
str_three = "python36"
str_four = "WelcoMe"
str_five = "9.87"

is_alpha = str_one.isalnum()
print("the given string is alpha: {}".format(is_alpha))

is_not_alpha = str_one.isnumeric()
print("the given string is not alpha: {}".format(is_not_alpha))

is_lower = str_three.islower()
print("the given string is lower {}".format(is_lower))

is_upper = str_four.isupper()
print("the given string is upper {}".format(is_upper))

is_alphanum = str_three.isalnum()
print("the given string is alphanum {}".format(is_alphanum))

is_dec = str_five.isdecimal()
print("the given string is decimal{}".format(is_dec))


# string concatenation
str1 = "abhi"
str2 = "shek"
str3 = " "
str4 = "S"

str_con = str1 + str2 + str3 + str4
print("the concat is {}".format(str_con))

# string length
str_len = "the python programming is simple"
lenght = len(str_len)
print("the length of the given given string is : {}".format(lenght))

str_dt = ("abhi", "abhishek", "abhiram")
str_a = str_dt[0][::-1]
str_b = str_dt[1][::-1]
str_c = str_dt[2][::-1]
print("the rev of index a is {}".format(str_a))
print("the rev of index a is {}".format(str_b))
print("the rev of index a is {}".format(str_c))


    # string reverse
str_res = "the python programing"
string_op = str_res[::-1]
print("the reverse value of given string is {}".format(string_op))