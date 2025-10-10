In Python, a string can be split on a delimiter.

# Example:

    a = "this is a string"
    a = a.split(" ") # a is converted to a list of strings. 
    print(a)
    ['this', 'is', 'a', 'string']

Joining a string is simple:

    a = "-".join(a)
    print(a)
    this-is-a-string 
# Task

You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Input Format

A string consisting of space separated words.

# Output Format

A string of - separated words.

# Sample Input 0

    this is a string

# Sample Output 0

    this-is-a-string