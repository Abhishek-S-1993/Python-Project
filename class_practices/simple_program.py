# program to add two numbers
num1 = 10
num2 = 15
sum = num1 + num2
print("the sum of {0} and {1} is {2}".format(num1, num2, sum))

lst_a = [1, 2, 3, 4, 5]
lst_b = [[11, 12], [13,14]]
lst_c = dict(zip(lst_a, lst_b ))
print("the zip file of given file is {}".format(lst_c))


lst1 = ["vegetables", "fruits"]
lst2 = [["beans", "carrot"], ["Apple", "Orange"]]
dict3 = dict(zip(lst1, lst2))
print("The value of dictionary from two lists is {}".format(dict3))


lstx = ["abhi", "mulbagal"]
lsty = [["Maruthi Nagar"], ["kolar", "karnataka"]]
dict4 = dict(zip(lstx, lsty))
print("the practice mode is {}".format(dict4))


lsta = [2,4,6]
lstb = [3,4,5]
lstc = [0,1,2]

lst_sum_a_b = []
lst_sum_a_c = []

for i in range(len(lsta)):
    print(i)
    lst_sum_a_b.append(lsta[i]+lstb[i])
    print(lst_sum_a_b)
    lst_sum_a_c.append(lsta[i]+lstc[i])
    print(lst_sum_a_c)
print(lst_sum_a_b)
print(lst_sum_a_c)






# lstx = [1,2,3]
# lsty = [4,5,6]
# lstz = [7,8,9]
#
# for i in lstx:
#     print(i)
#     for j in lsty:
#         print(i, j)
#     for z in lstz:
#         print(i, z)
#
#
# x = 10
