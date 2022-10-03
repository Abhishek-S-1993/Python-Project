# Set
"""Set is a group of elements enclosted between {},
where set is immutable, unordered and unindexed.
Set doesn't contain duplicates"""

set1 = {"a", "b", "c", "d"}
print("the given set is {}".format(set1))

lst = [1,2,3,4,5,6]
lst_set = set(lst)
print("The value of list to set is {}".format(lst_set))
length = len(lst_set)
print("the length is {}".format(length))

type_set = type(set1)
print("the given type is {}".format(type_set))

# add and update in set

lst_set.add("7")
print("after adding of the element is {}".format(lst_set))

lst_set.update("8", "9")
print("after updating the list is {}".format(lst_set))

# remove, discard and pop and clear in sets

"""
** Remove will raise error if element does not exist
** discard will not raise error if element does not exist
** pop will delete last element from set, but set is unordered and cannot know which element is getting removed
"""

# lst_set_rem = lst_set.remove()
# print("after removing the given element is {}".format(lst_set_rem))

# lst_set_discard = lst_set.discard("1")
# print("after discarding the given element is {}".format(lst_set_discard))
#
# lst_set_pop = lst_set.pop()
# print("after pop the given element is {}".format(lst_set_pop))

# union and intersection
set1 = {"a", "b", 1, 2}
set2 = {"c", "d", "a"}

union_set  = set1.union(set2)
print("the union of two set are {}".format(union_set))

inter_set = set1.intersection(set2)
print("the intersection of two set are {}".format(inter_set))

