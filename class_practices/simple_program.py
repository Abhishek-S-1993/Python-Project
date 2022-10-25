# program to add two numbers
import value as value

num1 = 10
num2 = 15
sum = num1 + num2
print("the sum of {0} and {1} is {2}".format(num1, num2, sum))

lst_a = [1, 2, 3, 4, 5]
lst_b = [[11, 12], [13, 14]]
lst_c = dict(zip(lst_a, lst_b))
print("the zip file of given file is {}".format(lst_c))

lst1 = ["vegetables", "fruits"]
lst2 = [["beans", "carrot"], ["Apple", "Orange"]]
dict3 = dict(zip(lst1, lst2))
print("The value of dictionary from two lists is {}".format(dict3))

lstx = ["abhi", "mulbagal"]
lsty = [["Maruthi Nagar"], ["kolar", "karnataka"]]
dict4 = dict(zip(lstx, lsty))
print("the practice mode is {}".format(dict4))

lsta = [2, 4, 6]
lstb = [3, 4, 5]
lstc = [0, 1, 2]

lst_sum_a_b = []
lst_sum_a_c = []

for i in range(len(lsta)):
    print(i)
    lst_sum_a_b.append(lsta[i] + lstb[i])
    print(lst_sum_a_b)
    lst_sum_a_c.append(lsta[i] + lstc[i])
    print(lst_sum_a_c)
print(lst_sum_a_b)
print(lst_sum_a_c)

lstx = [1, 2, 3]
lsty = [4, 5, 6]
lstz = [7, 8, 9]

for i in lstx:
    print(i)
    for j in lsty:
        print(i, j)
    for z in lstz:
        print(i, z)

x = 10

lst_a = [2, 6, 9, 13, 22, 10, 33, 21, 4, 8]

evenlst = []
oddlst = []

for i in lst_a:
    if i % 2 == 0:
        evenlst.append(i)
    else:
        oddlst.append(i)

print("The even list is {}".format(evenlst))
print("The odd list is {}".format(oddlst))

# 10 Write a function to reverse a list

lst = [1, 5, 6, 7, 9, 8]
print("The given list is {}".format(lst))
lst_rev = lst[::-1]
print("The reverse a list is {}".format(lst_rev))

# 9 Count the number of times "e" occurred in given string
str = "welcome to college"
print("The given string is {}".format(str))
str_count = str.count("e")
print("The count of given element e is {}".format(str_count))

# Find whether the given string is palindrome or not
# palindrome = input("Enter the String : ")
# str_rev_palindrome = palindrome[::-1]
# if str_rev_palindrome == palindrome:
#     print("This is palindrome")
# else:
#     print("This is not palindrome")

# Write a function for descending order of a list
lst_descending = [1, 2, 3, 4, 5]
lst_des = lst_descending[::-1]
print("The descending order of a list is {}".format(lst_des))

# Find the list of even and list of odd from given list

lst_num = [5, 8, 9, 6, 7, 3, 2, 55, 44, 88, 65]
print("The given list is {}".format(lst_num))
even_num = []
odd_num = []

for i in lst_num:
    if i % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)

print("The even number lst is {}".format(even_num))
print("The odd number list is {}".format(odd_num))

lst = [" ABC ", " hcb", "xyz"]
print(lst)
for i in range(len(lst)):
    if " " in lst[i]:
        str = lst[i].replace(" ", "")
        lst[i] = str
print(lst)

# remove duplicate
lst = [25, 20, 9, 25, 20, 20, 10]
print(lst)
lst_set = set(lst)
# print(lst_set)
set_lst = list(lst_set)
print(set_lst)

# Print the elements of list which is starting and ending with same letter
lst = ["malayalam", "area", "dog"]

for i in lst:
    if i[0] == i[-1]:
        print(i)

# Print the value of string which is in the place of multiples of string

str = "welcome to python"
for i in range(3,30,3):
    print(str[i])

# reversing value

number = 48
dif_val = str(number)
diff_value = dif_val[::-1]
dif_int = int(diff_value)
diff = number - dif_int
print("the diff value is {}".format(diff))



# Write a Python function to find the Max of three numbers.
def max_of_two(x, y):
    if x > y:
        print(x)
    else:
        print(y)

def max_of_three(x,y,z):
    return max_of_three(x, max_of_two(y,z))
print(max_of_three(6,9,10))




