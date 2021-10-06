import sys
import math
import random
import threading
import time
from functools import reduce

# tuples
# are just like lists but are immutable/cannot be changed.

t1 = (1, 3.14, "Tyler")
# Get the length of the tuple
print("Length", len(t1))
# Get them by indeces 
print("1st", t1[0])
# Get the last by index
print("Last", t1[-1])
# Get 1st 2 
print("1st 2", t1[0:2])
# Get every other one
print("Every other", t1[0:-1:2])
# Reverse it
print("Reverse", t1[::-1])


#Dictionaries
#Lists of key value pairs
#Duplicate keys aren't allowed

heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne"
}

# Another way to define dictionaries
#villains = dict([
#    ("Lex Luthor", "Lex Luthor"),
#    ("Loki"), ("Loki")
#])

# GEt the number of items using length again

print("Length", len(heroes))
# Get a value by passing a key
print(heroes["Superman"])
# Add additional
heroes["Flash"] = "Barry Allan"
#change a value
heroes["Flash"] = "Barry Allen"
# Get a list of tuples from a dictionary
print(list(heroes.items()))
# Get lists and keys
print(list(heroes.keys()))
#Delete these items
del heroes["Flash"]
#remove a key and return it
print(heroes.pop("Batman"))
# search to see if a specific heroe exists
print("Superman" in heroes)
#cycle through heroes
for k in heroes: 
    print(k)

#Be able to get values
for v in heroes.values():
    print(v)

#formatted printing with dictionary mapping
d1 = {"name": "Bread", "price": .88}
print("%(name)s costs $%(price).2f" % d1)



#Sets
#a set is a list that is unordered only has unique values, and while values can change, the values themselves are immutable

s1 = set(["Tyler", 1])
s2 = {"Paul", 1}

#prints length of s2
print("Length", len(s2))
#join sets
s3 = s1 | s2
print(s3)

#add values
s3.add("Doug")
#discard
s3.discard("Tyler")
#remove a random value
print("Random", s3.pop())
#add values
s3 |= s2
#return common values only items that arein both s2 and s1
print(s1.intersection(s2))
#get all unique values
print(s1.symmetric_difference(s2))
# get values from s1 that aren't in s2
print(s1.difference(s2))
#clear different values in a aset
s3.clear()
#frozen set is a set that cannot be changed in anyway
s4 = frozenset(["Paul", 7])

#functions
#provide code reuse organizations and much more.


def get_sum(num1: int = 1, num2: int = 1 ):
    return num1 + num2


print(get_sum(5, 4))

#accept multiple values which we have no idea how many
def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(get_sum2(1, 2, 3, 4))

#more complicated ones
#return multiple values

def next_2(num):
    return num + 1, num + 2

i1, i2 = next_2(5)
print(i1, i2)


#lets say we would like to make a function that makes a function that multiplies by a given value
def mult_by(num):
    #anonymous/unnamed function
    return lambda x: x * num
print("3 * 5 =", (mult_by(3)(5)))

#pass a function to a function
def mult_list(list, func):
    for x in list:
        print(func(x))
mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)