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


def mul(num4: int, num5: int):
    num6 = num4 * num5
    return num6


num4 = 8
num5 = 9

multi = mul(num4, num5)
print("the total sum of the given num is {} ".format(multi))


def div(num9: int, num10: int):
    num8 = num9 / num10
    return num8


num9 = 10
num10 = 5

division = div(num9, num10)
print("the division of two number is {}".format(division))


def my_fun(food):
    for x in food:
        print(x)


fruit = ["apple", "banana", "grapes"]
my_fun(fruit)


def fun_veg(foods):
    for i in foods:
        print(i)


vegetables = ["carrot", "radish", "beetroot"]
fun_veg(vegetables)


def my_function(name, number="", address="NA"):
    print("name:" + name)
    print("number : " + number)
    print("address : " + address)


my_function("abhi", "9620845431", "MBL")

fruits = "7"
fruits = fruits + "0"
eggs = int(fruits) + 3
print(float(eggs))

print("\U0001F600")
print("\U0001F618")
print("\U0001F917")
print("\U0001F62A")
print("\U0001F637")
print("\U0001f600")
print("\U0001F607")
print("\U0001F910")
print("\U0001F612")


def sun(num1: int, num2: int):
    num3 = num1 + num2
    return num3


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
sun = add(num1, num2)
print("The sum of {} and {} is {}".format(num1, num2, sun))


def area(length: float, breath: float):
    area = length * breath
    return area


length = int(input("Enter the length : "))
breath = int(input("Enter the breath :"))
total = area(length, breath)
print("The area of the given yard : {}".format(total))
