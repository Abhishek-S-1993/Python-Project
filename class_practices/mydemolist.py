# list

lst = [10,20,30,40,50]
print("the give 1st list elements are {}".format(lst))

# list indexing
lst_one = ["abhi", "10", "python", "data", "50", 90, 20, "session"]
print("the 2nd given list is {}".format(lst_one))
lst_ind_one = lst_one[4]
print("the 4th element of the given list is {}".format(lst_ind_one))

lst_ind_two = lst_one[6]
print("the 6th element of the given list is {}".format(lst_ind_two))

lst_ind_three = lst_one[2]
print("the 2nd element of the given list is {}".format(lst_ind_three))

# reverse indexing
lst_two = [20, 30, 40, 50, "abhi", "cambridge", "abc", 55, 88, 44]
print("the 3nd given list is {}".format(lst_two))
lst_rev_one = lst_two[-3]
print("the -3rd element value in the given list is {}".format(lst_rev_one))

lst_rev_two = lst_two[-5]
print("the -5th element value in the given list is {}".format(lst_rev_two))

lst_rev_three = lst_two[-8]
print("the -8th element value in the given list is {}".format(lst_rev_three))

#list slicing

lst_three = [10, 20, 30, "abc", "bang", "bad", "good", "50", "70"]
print("the 4th given list is {}".format(lst_three))

lst_sl_one = lst_three[3:5]
print("the value between 3 to 5 is {}".format(lst_sl_one))

lst_sl_two = lst_three[4:9]
print("the value between 4 to 9 is {}".format(lst_sl_two))

lst_sl_three = lst_three[0:7]
print("the value between 0 to 7 is {}".format(lst_sl_three))

lst_one = [1 ,2 ,3,4,5]
lst_two = [6,7,8,9,10]
lst_cat = lst_one+lst_two
print("the concatenation  of two list is {}".format(lst_cat))

lst_ele = [4,54,9,4,1,2,3,99,44,83,39,55]
lst_ele.sort()
print("the ascending order od the given list is {}".format(lst_ele))
lst_ele.reverse()
print("the descending order of given list is {}".format(lst_ele))

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
lst1 = [['abhi','ram'], ['abhi',"shek"],['mulbagal']]
print("Accessing the elements from given list is {}".format(lst1))
print(lst1[0][0])
print(lst1[0][1])
print(lst1[1][0])
print(lst1[1][1])

# List length
lst2 = [1,2,3,4,5,6,7,8,9,11,12,13,14,15]
lst_len = len(lst2)
print("the length of the list is {}".format(lst_len))

#Using append() method

lst3 = [1,2,3,4,5,"abhi", "ram", 6,7,8,9]
print("the given list is {}".format(lst3))
lst3.append(10)
lst3.append("mbl")
lst3.append("abhishek")
print("the given list after adding element is {}".format(lst3))


# Using insert() method
lst4 = [11,12,13,14,15,22,34,345,65]
print("the given list is {}".format(lst4))
lst4.insert(4, 456)
lst4.insert(1, 23)
lst4.insert(3,99)
print("the given list after inserting element is {}".format(lst4.insert))


#Using extend() method
"""this method is used to add multiple elements at the same time at the end of the list"""
"""append() and extend() methods can only add elements at the end"""

lst5 = [1,2,3,4,5]
print("the given list is {}".format(lst5))
lst5.extend([8, "mbl", "kolar"])
lst5.extend([121,123,456,567,898])

print("the given list after extending element is {}".format(lst5))


#Reversing a List
lst_rev = [13,45,78,89,561, 'mom','daddy']
lst_rev.reverse()
print(lst_rev)

#Using remove() method
"""Removing Elements from the List"""

lst6 = [1,2,3,4,5,6,7,8,9]
print("the given list is {}".format(lst6))
lst6.remove(9)
lst6.remove(8)
lst6.remove(7)
lst6.remove(6)
print("the given list after removing the given element is {}".format(lst6))

# list concatenation
lst_A = [1,2,3,4,5]
lst_B = [6,7,8,9]
lst_cat = lst_A+lst_B
print("the concatenation of two list are {}".format(lst_cat))

# appending the empty list

lst_empty = []
print(lst_empty)
lst_empty.append("abhi")
print(lst_empty)

# max and min value in list

lst_num = [11,12,13,14,15,16,17,18,19,20]
list_max = max(lst_num)
print("the max num in given list is {}".format(list_max))

lst_min = min(lst_num)
print("the min num in given list is {}".format(lst_min))

# finding index of an object
lst_obj = [2,3,4,5,"abhi","ram","abhishek"]
lst_f_obj = lst_obj.index(5)
print("the index of given object is {}".format(lst_f_obj))

# inserting an object with the reference of index value
lst_obj.insert(3,"Abhi")
print("the value of list after inserting is {}".format(lst_obj))

# pop element from list

lst_obj.pop()
print("the value of given list after pop is {}".format(lst_obj))

# zip in list
lsta = [1,2,3]
lstb = [4,5,6]
lst_zip = list(zip(lsta,lstb))
print("the value after zip 2 list is {}".format(lst_zip))

# count of element in the list
lst_count = ["the india are more innocent and power full"]
lst_c = lst_count[0].count("i")
print("the length of list is {}".format(len(lst_count)))
print("the count of given element is {}".format(lst_c))

lsta = ["a", "i", "b", "i"]
lsta_cnt = lsta.count("i")
print("the count of i in list is {}".format(lsta_cnt))

# sum of element in a list
lst_int = [1,2,3,4,5,6,7,8,9]
list_sum = sum(lst_int)
print("the total sum of given list is {}".format(list_sum))

# sorting of elements in a list
lst_sort = [12,55,85.1,66,20,45,33,10,52,88,]
print("the element before the sort is {}".format(lst_sort))
lst_sort.sort()
print("the elements of the sort is {}".format(lst_sort))

# converting from list to tuple
lst = [1,"a",2,"b",3,"c"]
lst_tup = tuple(lst)
lst_type = type(lst_tup)
print(lst_type)

# converting to tuple to list
tup = (1,2,3,4,5,6,7)
tup_lst = list(tup)
tup_type = type(tup_lst)
print(tup_type)






