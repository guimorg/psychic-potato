# Python and Name Assignment

## Python Assignment

One of the things that really messed me up when trying to understand some errors my programs had was involving Python’s Assignment (or the equal sign ‘=’).

It is very interesting to notice that many people still have a wrong perception of how Python works under the hood and a common misperception involves this topic.

We’ll try understanding better all of this (memory management) using Python and C++ code (thanks to [Scott Lobdell’s post](http://scottlobdell.me/2013/08/understanding-python-variables-as-pointers/)).

ps: sorry for my C++ code, it's been a long time since I last made a code snippet.

### Assignment 1

You'll find a comparison of memory management in Python and C++ in the files `assignment/python_folder/assignment_1.py` and `assignment/python_folder/assignment_1.cpp`.

If you run both files you'll see that while in Python the equal operator made assigned the same value to both names in C++ the same operator created and allocated memory for the specific variable.

Also notice that in C++ both variables were assigned next to each other in the memory, one after the other, taking 4 bytes in memory. (We'll see something similar in another Assignment file).

### Assignment 2

In this example we only check if the scope of the variable in some way affects how memory allocation is done (i.e. if we see another behaviour regarding assignment) `assignment/python_folder/assignment_2.py`.

You'll see no changes in the behaviour of the code, meaning that some names ('variables') that go out of scope still do not free up memory of the program.

### Assignment 3

You'll find a comparison of memory management in Python and C++ in the files `assignment/python_folder/assignment_3.py` and `assignment/python_folder/assignment_3.cpp`.

Here we are looking at the behaviour of lists (although lists are not the *same thing* as vectors in C++ we are safe to compare them).

We'll see that in C++ the 'head', i.e. first value memory address, of the 'list' is the same as the whole list (mainly because arrays are pointers).

In Python the behaviour is not the same but the concept is similar: each value in the list actually holds a reference to the value (i.e. list[0] points to the value and do not hold the value). But we do not see the list having the same address as the first value, because it is itself another container (holding containers, lol).

### Assignment 4

You'll find a comparison of memory management in Python and C++ in the files `assignment/python_folder/assignment_4.py` and `assignment/python_folder/assignment_4.cpp`.

Here we explore more what we saw in _'Assignment 3'_, we iterate through each value of the list and check its memory address.

The behaviour in C++ is the same as we expect: each value separated by 4 bytes and arrange one after the other.

In Python everything looks fuzzy. The list itself (a container) holds a memory address but each value holds a different memory address following no logic order.

### Assignment 5

You'll find a comparison of memory management in Python `assignment/python_folder/assignment_5.py`.

Here we explore a popular problem that happens when we are dealing with dictionaries in Python and want to change some values.

When we assign a name to an existing dict we are actually pointing to that dictionary (mainly because `dict`s are mutable objects in Python). We can se that, in the first snippet, both objects have the same memory address.

When we make the use of the copy library and make a shallow copy (`copy.copy()` which is the same as `dict.copy()` method) the object holds a new place in the memory but all of the references point to the same place in the memory. So changes made to a key will actually be made in both dictionaries EVEN THOUGH they do not hold the same place in memory.

The right way to do it, which still have a weird behaviour, is making a deep copy of the object (`copy.deepcopy()`). In the last snippet we see that not only the object holds a new place in memory but that key values' also hold a new place in memory. Watch it closely because the key still holds the same place in memory (but, as changing keys in a dictionary is not trivial nor easy we can rest safely).

### Assignment 6

You'll find a comparison of memory management in Python `assignment/python_folder/assignment_6.py`.

Here we proceed the investigation using `copy.deepcopy()` but using mutable types (`list`s in the example). We can see the wanted behaviour desired.
