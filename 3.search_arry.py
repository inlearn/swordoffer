def find_num(matrix, number):
    found = False
    if not matrix:
        return found
    rows = len(matrix)
    columns = len(matrix[0])
    row = 0
    column = columns - 1
    while rows > row >= 0 and columns > column >= 0:
        if matrix[row][column] > number:
            column -= 1
        elif matrix[row][column] < number:
            row += 1
        else:
            return True
    return False


if __name__ == "__main__":
    array1 = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    # print(find_num(array1, 3))
    import cProfile
    cProfile.run("find_num(array1, 3)")
