#check for matrix indentity 


row, col = list(map(int,input().split()))

if(row != col ):
    print("Not an identity matrix")

matrix = []
for r in range(row):
    new_list = list(map(int, input().split()))
    matrix.append(new_list)

ctr = 0
for r in range(row):
    for c in range(col):
        if r == c :
            if matrix[r][c] != 1:
                ctr = 1
if ctr == 1:                
    print("Not an identity matrix")
else:                    
    print("Identity matrix")


# input 
# 3 3
# 1 0 0
# 0 0 0
# 1 0 1

# output
# Not an identity matrix


# input 
# 3 3
# 1 0 0
# 0 1 0
# 0 0 1

# output
# identity matrix

