# for loop

str = "Abhi"
for i in str:
    print(i)

lst = [1, 2, 3, 4]
for i in lst:
    print(i)

seta = {"a", "b", "c", "d"}
for i in seta:
    print(i)

dict_a = {1: "a", 2: "b", 3: "c", 4: "d"}
for k, v in dict_a.items():
    print(k)
    print(v)

tpl = (11, 22, 33, 44, 55)
for j in tpl:
    print(j)

# String reversing without using inbuilt function and without using slicing
str_d = "Deekshitha"
rev_st = ""
for i in str_d:
    rev_st = i+rev_st
    print("the String reversing is {}".format(rev_st))


# Assigment
str_a = "welcome"
str_b = "to"
str_c = "python"

rev_str = ""
for i in str_a:
    rev_str = i+rev_str
    print(rev_str)
for j in str_b:
    rev_str = j+rev_str
    print(rev_str)
for k in str_c:
    rev_str = k+rev_str
    print(rev_str)

str_ass = "welcome to python"
str_split = str_ass.split()
print(str_split)
str_pr = str_split[0][::-1], str_split[1][::-1], str_split[2][::-1]
print(str_pr)
# lst_str = str(str_pr)
# print(lst_str)

for letter in "python":
    print("the given character is :", letter)


for number in (1,2,3,4,5):
    print("the given number are", number)
    if number >= 3:
        print("the given number is greater")
    else:
        print("the given number is small")

str_fruits = ["banana", "apple", "orange", "grapes"]
for i in str_fruits:
    print(i)
    if i == "apple":
        pass
        print(i)

# Ranger Function

for i in range(3):
    print(i)

for i in range(4,9,12):
    print(i)


for x in range(6):
    if x == 3:
        break
        print(x)
    else:
        print(" finally done")

str_x = ["red", "blue", "green", "pink", "white"]
str_y = ["danger", "peace", "water", "lips", "fire"]

for i in str_x:
    for j in str_y:
        print(i, j)

# lst_a = [1,2,3]
# lst_b = [4,5,6]
# lst_c = [7,8,9]

# for i in lst_a:
#     for j in lst_b:
#         print(i,j)
#         for k in lst_c:
#             print(i,j)
#             print(i,k)
#             print(i,j,k)

number = int(input("Enter the number : "))
if number % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")


length = int(input("Enter the length :"))
width = int(input("Enter the width :"))
square_feet = length*width

print("The length {} and width {} so total square feet is {}".format(length, width, square_feet))