# Flatten a nested list

nested_list = [[1,2,4],[4,7,6],[9,8,2]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)