def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    res = []
    fil = open(path, "r")
    for i in fil:
        res.append(i[:-1])
    return res

def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    visibility = 1
    highest = input_line[1]
    for i in range(2,6,1):
        if input_line[i] > highest:
            visibility += 1
            highest = input_line[i]
    return visibility == pivot