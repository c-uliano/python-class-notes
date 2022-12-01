# going over some basics in office hour

# 
some_number = 5
print(some_number * 3)

# 
name = 'River'
age = 29
# typecasting or conversion, changing that integer into a string. 
print("My name is " + name + " and I am " + str(age) + " years old")
# using an f-string
print(f"My name is {name} and I am {age} years old") 

# ! saving a random number bewteen 2 and 5 and saving it in a variable. It's not working, why is it now working?? will have to rewatch the lecture hour, did I do something wrong?
# * ANSWER: you need to import the module file for this to work
import random
random_num = random.randint(2,5)
print(random_num)

# 
