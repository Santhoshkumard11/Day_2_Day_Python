#find the trace and normal of a matrix
import math

row, col = list(map(int,input().split()))

if row != col:
    print("Invalid Input")

else:
    matrix = []
    for r in range(row):
        new_list = list(map(int, input().split()))
        matrix.append(new_list)

    total_trace, total_normal = 0, 0
    for r in range(row):
        for c in range(col):
            total_normal += matrix[r][c] * matrix[r][c]
            if c==r :
                total_trace += matrix[r][c]
                total_normal += matrix[r][c] * matrix[r][c]

    print(math.sqrt(total_normal),total_trace)

#input
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

# output
# 19.79898987322333 15