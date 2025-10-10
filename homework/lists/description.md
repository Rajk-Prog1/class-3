Before working on this assignment, check out the section on lists in this [tutorial](https://github.com/Rajk-Prog1/prog1-teaching-materials/blob/main/tutorials/python_basic/basics.ipynb).

Consider a list (list = []). You can perform the following commands:

- insert **i **e**: Insert integer **e** at position **i**.
- return: Return the list.
- remove **e**: Delete the first occurrence of integer **e**.
- append **e**: Insert integer **e** at the end of the list.
- sort: Sort the list.
- pop: Pop the last element from the list.
- reverse: Reverse the list.

# Task

Initialize an empty list. Iterate through each command in your commands list (given as input) in order and perform the corresponding operation on your list.

# Example
commands = ["append 1", "append 2", "insert 3 1", "return"]

- Initialize an empty list **arr**. Contents of **arr** = [].
- append 1: Append 1 to the list. Contents of **arr** = [1].
- append 2: Append 2 to the list.Contents of **arr** = [1, 2].
- insert 3 1 : Insert 3 at index 1. Contents of **arr** = [1, 3, 2].
- return : Return **arr**.

Output:

    [1, 3, 2]
# Input Format

A list containing the commands described above as strings.

# Constraints

The elements added to the list must be integers.

# Output Format

A list containing integers.

# Sample Input 0

    insert 0 5
    insert 1 10
    insert 0 6
    remove 6
    append 9
    append 1
    sort
    pop
    reverse
    return
# Sample Output 0

    [9, 5, 1]