# Create a matrix using lists and access specific rows and columns.

matrix = [[7,5,9],[4,3,9],[8,4,6]]

row1 = matrix[0]
column1 = [row[0] for row in matrix]

print("First row:", row1)
print("First column:", column1)
element = matrix[2][1]  
print("Element at (2, 1):", element)