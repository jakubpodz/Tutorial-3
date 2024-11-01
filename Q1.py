# Create a new list called 'my_coordinates'
# Using a for loop:
# For the following list of strings, find the start and end position of each of the list items in the sentence using the find command.
# Then populate this list with a tuple of (start location, end location) for each value in my_list   
# Using a while loop, loop through each word in my_string until you find the word contined in the variable 'target'. 
# Set a variable target_loc equal to number of iterations of the while loop completed 
# (i.e. the location of the word in the sentance) 
# Repat the exercise with a new while loop until you find the word contined in the varaiable 'target2'. 
# Set a variable target2_loc equal to number of iterations of the while loop completed 
# (i.e. the location of# the word in the sentance) or -1 if the word is not found (beware of infinite loops!

my_string = 'Today we are learning about conditionals, loops and functions'
my_list = ['conditionals', 'loops', 'functions']
target = 'loops'
target2 = 'variables'

my_coordinates = []

for i in my_list:
    start = my_string.find(i)
    if start != -1:
        end = start + len(i)
        my_coordinates.append((start, end))
print(my_coordinates)



target_loc = 0

words = my_string.split()

while target_loc < len(words):
    if words[target_loc] == target:
        break
    else:
        target_loc += 1
    
print(target_loc)


target_loc2 = 0

while target_loc2 < len(words):
    if words[target_loc2] == target2:
        break
    else:
        target_loc2 += 1
if target_loc2 == len(words):
    target_loc2 = -1
    
print(target_loc2)








