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


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in board:
        if '?' in i:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(1,6,1):
        for j in range(1,6,1):
            for m in range(1,6,1):
                if board[i][j] == board[i][m] and j != m:
                    return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(1,6,1):
        if board[i][0] != '*':
            if left_to_right_check(board[i], int(board[i][0])) == False:
                return False
        if board[i][-1] != '*':
            if left_to_right_check(board[i][::-1], int(board[i][-1])) == False:
                return False
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(1,6,1):
        for j in range(1,6,1):
            for m in range(1,6,1):
                if board[j][i] == board[m][i] and j != m:
                    return False

    for i in range(1,6,1):
        if board[0][i] != '*':
            summa = ''
            for j in range(7):
                summa += board[j][i]
            if left_to_right_check(summa, int(board[0][i])) == False:
                return False
        if board[-1][i] != '*':
            summa = ''
            for j in range(7):
                summa += board[j][i]
            if left_to_right_check(summa[::-1], int(board[-1][i])) == False:
                return False
    return True