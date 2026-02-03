# 1. Create a tuple of at least 5 subjects and print them using a loop.
import this

subjects = ("Maths", "Science", "English", "History", "ICT")
for subject in subjects:
    print(subject)
# 2. Create two sets of numbers and perform all set operations.
set_one = {1, 2, 4, 5}
set_two = {5, 3, 2, 1, 10, 9, 11}

print("Union:", set_one | set_two)
print("Intersection:", set_one & set_two)
print("Difference:", set_one - set_two)
print("Symmentric Difference:", set_one ^ set_two)

# 3. Create a dictionary to store student details and update/remove values.

address = {"city": "new york", "state": "texas"}

student = {"name": "kamal", "age": 23, "department": "ICT", "address": address}

student.update({"name": "Suraj"})
print(student)
student.pop("name")
print(student)

# 4. Create a nested dictionary to represent a student and their marks.
marks = {"maths": 54, "science": 89, "ict": 65, "sinhala": 45}
student.update({"marks": marks})
print(student)


# 5. Write a program to convert a tuple into a list, modify one element, and convert it back
# into a tuple.
#
x = ("apple", "banans", "orange")
y = list(x)
y[1] = "kiwi"
print(y)
x = tuple(y)
print(x)


# 6. Write Python code to join two tuples and display the result.
tuple_one = (1, 2, 3, 4, 5)
tuple_two = (5, 4, 5, 3, 1)
join_tuple = tuple_one + tuple_two
print(join_tuple)

# 7. Write code to add multiple elements to an existing set.
this_set = {"ai", "maths"}
this_set.add("something")
this_set.update({"new", "old"})
print(this_set)

# 8. Create a tuple with mixed data types and print its length.
tuple_len = (1, 2, 3, "kite", "gomez", "julio")
print(len(tuple_len))

# 9. Write a program to iterate through a tuple using index-based looping.
iterate_tuple = ("kamal", "dumal", "hashi", "sachi")
for i in range(len(iterate_tuple)):
    print(iterate_tuple[i])

# 10. Write Python code to perform union, intersection, difference, and symmetric difference
# on two sets.
new_set_one = {"kamal", "dumal", "lahiru"}
new_set_two = {"kamal", "julio", "panke"}
print(new_set_one | new_set_two)
print(new_set_one & new_set_two)
print(new_set_one - new_set_two)
print(new_set_one ^ new_set_two)

# 11. Write a program to check whether a given element exists in a set
exists_set = {"one", "two", "three", "four", "five"}
element = "one"
if element in exists_set:
    print("exist")
else:
    print("not exist")

# 12. Write Python code to check whether one set is a subset of another.
# The method checks if the set on the left {1, 2} fits entirely inside the set on the right {1, 2, 3}.
print({1, 2, 4}.issubset({1, 2, 3, 4, 5}))

# 13. Create two disjoint sets and verify whether they are disjoint.
set_a = {1, 2, 3}
set_n = {"a", "b", "c"}
result = set_a.isdisjoint(set_n)
print(result)

# 14. Write a program to create a nested set using frozenset.
frozen_set = frozenset({"soemthing", "in", "the", "way"})
print(frozen_set)

# 15. Write code to remove a key-value pair from a dictionary using pop().
employee = {
    "name": "panke",
    "age": 23,
    "city": "texas",
    "country": "USA",
}

print(employee.popitem())
print(employee)

# 16. Write a Python program to clear all elements from a dictionary.
employee.clear()
employee = {}

# 17. Write a program to merge two dictionaries into one.
dic_one = {"name": "milinda"}
dic_two = {"age": 23, "email": "example@mail.com"}
merge_dic = dic_one | dic_two
print(merge_dic)

# 18. Write Python code to create and access a nested dictionary.
address = {"city": "horana"}

parent_dic = {"name": "kumudu", "address": address}
print(parent_dic)

# 19. Write a program to sort a dictionary by its keys.
sort_dic = {"x": 45, "y": 23, "a": 100}
print(sorted(sort_dic.items()))

# 20. Write Python code to count the number of key-value pairs in a dictionary.
count = 0
for key, value in merge_dic.items():
    count += 1

print(count)
