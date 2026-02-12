import numpy as np


#numpy.sort( )
# Creating 5x4 array
array = np.arange(20).reshape(5, 4)
print(array)
print()

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]]
# If no axis mentioned, then it works on the entire array
print(np.argmax(array))

#Output: 19

#==========================================#

array = [
    [ 0,  11,  2,  3],
    [ 4,  5,  66,  7],
    [ 88,  9, 10, 11],
    [120, 13, 14, 15],
    [16, 17, 18, 190]
 ]

# If axis=0, then it works on each column, It will return index of maximum number on each column
print(np.argmax(array, axis=0))
#Output: [3 4 1 4]

# If axis=1, then it works on each row. It will return index of maximum number on each row
print(np.argmax(array, axis=1))
#Output: [1 2 0 0 3]

#==========================================#
#numpy.argsort( ):
array = np.array([28, 13, 45, 12, 4, 8, 0])
print(array)
# Output: [28 13 45 12  4  8  0]

print(np.argsort(array))
# Output: [6 4 5 3 1 0 2]

#==========================================#
#Using np.mean( )

list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

result = []
for i in range(len(list)):
    result.append(np.mean(list[i]))
print(result)

#Output: [np.float64(5.5), np.float64(30.6), np.float64(34.0)]

#==========================================#
#Adding Row using numpy.vstack( ). Used for Combining arrays row wise

array = np.array([
    [3, 2, 8],
    [4, 12, 34],
    [23, 12, 67]
])

newRow = np.array([2, 1, 8])
newArray = np.vstack((array, newRow))
print(newArray)

#Output: 
# [[ 3  2  8]
#  [ 4 12 34]
#  [23 12 67]
#  [ 2  1  8]]

#==========================================#
#Adding Column using numpy.column_stack( ). Used for Combining arrays column wise
array = np.array([
    [3, 2, 8],
    [4, 12, 34],
    [23, 12, 67]
])

newColumn = np.array([2, 1, 8])
newArray = np.column_stack((array, newColumn))
print(newArray)

# Output:
# [[ 3  2  8  2]
#  [ 4 12 34  1]
#  [23 12 67  8]]

#==========================================#
#Reverse attay Using numpy.flipud( )

array = np.array([3, 6, 7, 2, 5, 1, 8])
reversedArray = np.flipud(array)
print(reversedArray)

#Output: [8 1 5 2 7 6 3]

#==========================================#
#Multiply Array Using numpy.dot( ) 

a = np.array([2, 3])
b = np.array([4, 5])
print(np.dot(a, b))

# Output: 23       #=>  2*4 + 3*5 
#--------------

a = np.array([[1, 4],
              [5, 6]])

b = np.array([[2, 4],
              [5, 2]])

print(np.dot(a, b))

#Output: c  Logic: Top Right to Bottom-Left
# [
#   [22 12]
#   [40 32]
# ]

#Explanation:
# [0,0] -> (1×2) + (4×5) = 2 + 20 = 22
# [0,1] -> (1×4) + (4×2) = 4 + 8 = 12
# [1,0] -> (5×2) + (6×5) = 10 + 30 = 40
# [1,1] -> (5×4) + (6×2) = 20 + 12 = 32
#--------------

matrix1 = [
    [3, 4, 2],
    [5, 1, 8],
    [3, 1, 9]
]

matrix2 = [
    [1, 2, 1],
    [2, 1, 2],
    [1, 2, 1]
]

result = np.dot(matrix1, matrix2)
print(result)

#Output:
# [
#   [13 14 13]
#   [15 27 15]
#   [14 25 14]
# ]

#==========================================#
# Print Array example
n = 8

# Create a nxn matrix filled with 0
matrix = np.zeros((n, n), dtype=int)

# fill 1 with alternate rows and column
# Notation: start:stop:step. 
matrix[::2, 1::2] = 1
matrix[1::2, ::2] = 1

# Print the checkerboard pattern
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
    
# Output:
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0