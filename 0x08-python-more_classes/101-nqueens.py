#!/usr/bin/python3
# 101-nqueens.py
"""
In this task : All possible soltions to placing N
N non-attacking queens on an NxN chessbord.

Attributes:
    bord (list): A list of lists representing the chessbord.
    soltions (list): A list of lists containing soltions.

soltions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where r and c represent the row and column, respectively, where a
queen must be placed on the area chessbord.
"""
import sys


def init_bord(n):
    """Initialize a sized chessbord with 0's (nxn)."""
    bord = []
    [bord.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in bord]
    return (bord)


def bord_depcop(bord):
    """Return a depcop of a chessbord."""
    if type(bord) is not list:
        return list(map(bord_depcop, bord))
    return (bord)


def get_soltion(bord):
    """a function that return the list of lists representation"""
    soltion = []
    for r in range(len(bord)):
        for c in range(len(bord)):
            if bord[r][c] == "Q":
                soltion.append([r, c])
                break
    return (soltion)


def x_out(bord, row, col):
    """X out spots on a chessbord.

    others spots where non-attacking queens can no
    longer be played are X out.

    Arguments:
        bord (list): The current working chessbord .
        row (int): The row  was last played with queen.
        col (int): The column was last played with queen.
    """
    # 1
    for c in range(col + 1, len(bord)):
        bord[row][c] = "x"
    # 2
    for c in range(col - 1, -1, -1):
        bord[row][c] = "x"
    # 3
    for r in range(row + 1, len(bord)):
        bord[r][col] = "x"
    # 4
    for r in range(row - 1, -1, -1):
        bord[r][col] = "x"
    # 5
    c = col + 1
    for r in range(row + 1, len(bord)):
        if c >= len(bord):
            break
        bord[r][c] = "x"
        c += 1
    # 6
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        bord[r][c]
        c -= 1
    # 7
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(bord):
            break
        bord[r][c] = "x"
        c += 1
    # 8
    c = col - 1
    for r in range(row + 1, len(bord)):
        if c < 0:
            break
        bord[r][c] = "x"
        c -= 1


def recu_solve(bord, row, queens, soltions):
    """recul position solve an N-queens puzzle.

    Arguments:
        bord (list): The current working chessbord.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        soltions (list): A list of lists of soltions.
    Returns:
        ALL soltions possible
    """
    if queens == len(bord):
        soltions.append(get_soltion(bord))
        return (soltions)

    for c in range(len(bord)):
        if bord[row][c] == " ":
            tmp_bord = bord_depcop(bord)
            tmp_bord[row][c] = "Q"
            x_out(tmp_bord, row, c)
            soltions = recu_solve(tmp_bord, row + 1, queens + 1, soltions)
    return (soltions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bord = init_bord(int(sys.argv[1]))
    soltions = recu_solve(bord, 0, 0, [])
    for sol in soltions:
        print(sol)
