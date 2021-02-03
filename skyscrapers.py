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