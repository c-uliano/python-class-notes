"""
making an app to run in the terminal
cli = command line interface
"""
isActive = True 

# ? while loop, to keep going indefinately, until isActive is changed to False
while isActive:    
    line_input = input('Type in anything: ').strip() # ? strip() takes out all the extra spaces before & after text
    print(line_input)

    # those are 2 extra spaces with the line_input, because you need at least 3 words, but what if someone only writes 1 word? So now there are always at least 3 items in the list
    # ! no idea why the split(" ") does't cut those spaces out
    line_parts = (line_input + "  ").split(" ") # taking the string and creating a list. split(" "), any place there's a space, split the text. So that's how it knows to put each word to it's own key in the list

    command = line_parts[0]
    extra1 = line_parts[1]
    extra2 = line_parts[2]

    if command == 'quit':
        print( "Thanks for playing")
        isActive = False
    elif command == "walk": # walk 3 west, walk 15 north
        print(f"I am walking {extra1} spaces {extra2}.")
    elif command == 'cast-spell': # cast-spell fireball 3
        print(f"I am casting a {extra1} spell with {extra2} power.")
    else:
        print("Invalid command")