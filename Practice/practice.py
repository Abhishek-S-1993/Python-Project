# Write a Python function to find the Max of three numbers.
def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


print(max_of_three(55, 8, 45))


# Write a Python function to sum all the numbers in a list.

def sum_of_all(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


print(sum_of_all((1, 2, 3, 4, 5)))


# Write a Python function to multiply all the numbers in a list.

def mul(number):
    total = 1
    for z in number:
        total *= z
    return total


print(mul((8, 2, -3, 1, 7)))

# Write a Python program to reverse a string.
# String: "1234abcd"

str = "1234abcd"
str_rev = str[::-1]
print(str_rev)


# Write a Python function to check whether a numbers falls in a given range.
# o/p - 5 is in the range

def test_ranger(num):
    if num in range(3, 10):

        print(f"{num} is in the range")
    else:
        print("The number is outside the given range")


test_ranger(5)


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# String : 'The quick Brow Fox'

def string_test(strs):
    UPPERCASE = 0
    LOWERCASE = 0

    for c in strs:
        if c.isupper():
            UPPERCASE += 1
        elif c.islower():
            LOWERCASE += 1
        else:
            pass
    print("the original string is ", strs)
    print(("The upper case letter is {}".format(UPPERCASE)))
    print(("The lower case letter is {}".format(LOWERCASE)))


string_test('The quick Brown Fox')


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x


print(unique([1, 2, 3, 3, 6, 3, 4, 5, 8, 9]))


# Write a Python function that takes a number as a parameter and check the number is prime or not.

# def prime_test(n):
#     # for i in n:
#     #     if n == 1:
#     #         return False
#     #     elif n == 2:


    # if n == 1:
    #     return False
    # elif n == 2:
    #     return True
    # else:
    #     for n in range(2, n):
    #         if n % 2 == 0:
    #             return False
    #         return True





