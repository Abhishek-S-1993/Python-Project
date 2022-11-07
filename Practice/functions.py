def hello():
    print("Welcome to Python")


hello()


def for_loop(lst):
    for i in lst:
        print(i)


for_loop([1, 5, 6, 89])


# getting key and value separately
def dict_sept(dict_a):
    for keys, values in dict_a.items():
        print(keys)
        print(values)


dict_sept({"a": 1, "b": 2})


# Dividing the vegetable and fruits

def veg_fruit(dict_b):
    for k, v in dict_b.items():
        print(k)
        print(v)


veg_fruit({"vegetables": ["Tomato", "Onion"], "fruits": ["Apple", "Orange"]})


set_a = {1, 6, 0}
initial = 0
for k in set_a:
    initial = k
    print(k)
print(initial)


def str_rev(str_b):
    print("The given string is {}".format(str_b))
    rev_str = ""
    for i in str_b:
        rev_str = i + rev_str
    print("The value of reversed string is {}".format(rev_str))



str_rev("Deekshitha")


# Method calling
def fname():
    print("my first name ")


# method calling
fname()


# Sum of two number using method
def add(num1: int, num2: int):
    num3 = num1 + num2
    return num3


num1, num2 = 4, 5
ans = add(num1, num2)
print("the sum of two number is {} ".format(ans))


# mul of given numbers
def mul(num4: int, num5: int):
    num6 = num4 * num5
    return num6


num4 = 8
num5 = 9

multi = mul(num4, num5)
print("the total sum of the given num is {} ".format(multi))


# div of given number
def div(num9: int, num10: int):
    num8 = num9 / num10
    return num8


num9 = 10
num10 = 5

division = div(num9, num10)
print("the division of two number is {}".format(division))


# print thr fruit list
def my_fun(food):
    for x in food:
        print(x)


fruit = ["apple", "banana", "grapes"]
my_fun(fruit)


# print given veg list
def fun_veg(foods):
    for i in foods:
        print(i)


vegetables = ["carrot", "radish", "beetroot"]
fun_veg(vegetables)


def str_ind(in_st):
    str_rever = in_st[2]
    return str_rever