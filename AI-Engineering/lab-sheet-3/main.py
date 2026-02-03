# what is a tuple
# 1.2 creating a tupe
rgb = ("Red", "Green", "Blue")
print(rgb[0])
print(rgb[1])
print(rgb[2])
print(rgb)


# 1.3 Tuple with Duplicate Values and Length
this_tuple = ("apple", "Banana", "Cherry", "apple")
print(len(this_tuple))

# 1.4 Single-Item Tuple (Important!)
single_item_tuple = (3,)
print(type(single_item_tuple))


# 1.5 Tuple with Mixed Data Types

mixed_tuple = (1, "Two", False, "C", 3.15)
print(mixed_tuple)


# 1.6 Changing Tuple Values (Using List Conversion)
# Yes, exactly. The line $x = \text{tuple}(y)$ converts the object $y$ (which is likely a list, given the assignment $y[1] = \text{"kiwi"}$) into a tuple.Here is a breakdown of what is happening in that snippet:$y[1] = \text{"kiwi"}$: This updates the second item in the list $y$ to "kiwi". This step confirms $y$ is a list because you cannot change items in a tuple (tuples are immutable).$x = \text{tuple}(y)$: This takes the current content of the list $y$ and creates a new tuple named $x$ containing the same elements.
x = ("apple", "banana", "orange")
print(x)
y = list(x)
print(y)
y[1] = "kiwi"
print(y)
x = tuple(y)
print(x)

# 1.7 Adding Items to a Tuple
this_new_tuple = ("apple", "bananas", "kiwi")
this_new_tuple = this_new_tuple + ("grape",)
print(this_new_tuple)


# 1.8 Removing Items from a Tuple
remove_elements = ("apple", "banana", "orange")
y = list(remove_elements)
y.remove("apple")
remove_elements = tuple(y)
print(remove_elements)

# 1.9 Iterating Through Tuples
for item in remove_elements:
    print(item)

print("====================================")

for i in range(len(remove_elements)):
    print(i)
    print(remove_elements[i])

# 1.10 Joining Tuples

tuple_one = ("apple", "banana", "cherry")
tuple_two = (1, 2, 3, 4, 5)
tuple_three = tuple_one + tuple_two
print(tuple_three)


print(
    "=================================================== Sets ==============================================================="
)


# 2.2 Creating a sets
skills = {"python", "python", "java", "rust", "golang", "javascript", "typescript"}
empty_set = set()
print(skills)
print(type(empty_set))

# 2.3 Checking Empty Set
#
empty_set_ = set()
if not empty_set:
    print(f"{empty_set} is empty")

# 2.4 Iterating Through a Set
this_set = {"apple", "banan", "orange"}
for item in this_set:
    print(item)

# 2.5 Adding Elements
this_set.add("kiwi")
print(this_set)
this_set.update({"mango", "pear"})
print(this_set)


# 2.6 Removing Elements
color_set = {"yellow", "red", "pink", "brown"}
color_set.remove("pink")
print(color_set)

color_set.discard("red")
print(color_set)

print("---------------------")
# 2.7 Set Operations
a = {1, 2, 3}
b = {3, 5, 6}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


# 2.8 Subset and Superset
print({1, 2}.issubset({1, 2, 3}))
print({4, 5}.issubset({1, 2, 3}))
print({1, 2, 3}.issuperset({1, 2}))
print({1, 2, 3}.issuperset({1, 2, 4}))


# 2.9 Nested Sets (Using frozenset)
rainbow = ("red", "green", "blue")
other = ("white", "black")
nested_sets = set((frozenset(rainbow), frozenset(other)))
print(nested_sets)
print(type(nested_sets))


print(
    "============================================= Dictionary ==============================================================="
)
# 3.2 Creating Dictionaries
person = {"name": "john", "age": 20, "city": "New york"}


# 3.3 Accessing Values
name = "name"
print(person[name])
print(person.get("city"))

# 3.4 Adding and Updating Items
person["email"] = "john@example.com"
person["weight"] = 60
print(person)

# updating items
person.update({"weigth": 163})
print(person)


# 3.5 Iterating Dictionaries
for key, value in person.items():
    print(key, value)


# 3.6 Removing Items
person.pop("email")
person.popitem()
print(person)

# 3.7 Nested Dictionaries
address = {"city": "New York", "state": "NY"}
person = {"name": "Jessa", "address": address}
print(person["address"]["city"])

# 3.8 Sorting Dictionaries
d = {"c": 45, "b": 34, "a": 12}
print(sorted(d.items()))
