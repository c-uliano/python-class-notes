"""
? data structures
lists (otherwise known as arrays)
each item in list is an element
"""
shopping_list = ['marshmallows', 'graham crackers', 'chocolate']

index = 0

"""
? for loop
control statement, like if statements
for iteration
"""
# ? 0-9
# for index in range(10):
#     print(index)

# ? start at 2, up to 9, iterate by 2
# for index in range(2, 10, 2):
#     print(index)    

# ? decrement by 1, starts at 10, ends at 3
# for index in range(10, 2, -1):
#     print(index) 

# ? iterate through a list
# for index in range(len(shopping_list)):
#     print(shopping_list[index])

"""
? while loop
for when you don't know how long you have to iterate
"""
x = 1

while ( x <= 10 ):
    print ( x )
    x += 1

is_full = False
appetite = 5
eat_count = 0

while ( is_full == False ):
    
    print ( "is eating" )
    eat_count += 1

    if eat_count == appetite:
        is_full = True

print ( "I am full" )

"""
SPECS
    Create a collection of items the character can carry
    Add an 'inventory' action that displays all the items in inventory
"""