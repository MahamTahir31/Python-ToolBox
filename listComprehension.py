# Example 1

# Create list comprehension: squares
squares = [i**2 for i in range(10)]

print(squares)

# Example 2

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

matrix = [[col for col in range(5)] for row in range(5)]

# Printing the matrix
for row in matrix:
    print(row)

# Example 3 

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)

# Example 4

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [new_fellowship if len(new_fellowship)>=7 else "" for new_fellowship in fellowship]

# Print the new list
print(new_fellowship)

# Example 5

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}


# Print the new dictionary
print(new_fellowship)

