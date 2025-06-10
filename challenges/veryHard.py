def can_see_stage(list):
    for row in range(len(list)):
        for col in range(len(list[row])-1):
            if list[row][col] > list[row][col+1]:
                return False

    return True

def id_mtrx(n):
    if n == 0:
        return []
    size = abs(n)
    matrix = []
    for i in range(size):
        row = [0] * size
        if n > 0:
            row[i] = 1
        else:
            row[size - 1 - i] = 1
        matrix.append(row)
    return matrix
