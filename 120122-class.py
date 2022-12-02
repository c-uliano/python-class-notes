"""
SPECS for the app project
    iterate through a list of characters
    isolate the action functionality into a function
    randomly select action
"""

myList = [
    'marshmallows',
    'chocolate',
    'crackers'
]

# ? how do you mark stuff off of this list?
selected = [
    False,
    True,
    False
]

print("----------")

# ! somehow using an if statement in this string. Ternary? Look it up. Simplified if statement
for i in range(len(myList)):
    print(f"{myList[i]} {'has' if selected[i] else 'have not'} been selected")

print("----------")

# use objects
# * in python it's called a dictionary, but it's the same thing
singleItem = {
    "name": "milk",
    "selected": False
}

print(f"{singleItem['name']} {'has' if singleItem['selected'] else 'has not'} been selected")

print("----------")

# destructuring the object. Breaking down each key into a variable with it's value. Has to list out all the keys in the dictionary for this to work
name, selected = singleItem.values()
# so now you can do this
print(f"{name} {'has' if selected else 'has not'} been selected")

print("----------")

# dictionaries in a list, put it all together like this
newList = [
    {
        "name": "milk",
        "selected": False
    },
    {
        "name": "chocolate",
        "selected": True
    },
    {
        "name": "crackers",
        "selected": False
    }
]

# now iterate through that list of dictionaries (objects)
for item in newList:
    print(f"{item['name']} {'has' if item['selected'] else 'has not'} been selected")

"""
isolate action into a function
Functions
"""
print("----------")
def myFunction():
    print("Hello Sweetie")
myFunction()

print("----------")
def myFunctionTwo(name):
    print(f"Hello {name}")
myFunctionTwo("River")