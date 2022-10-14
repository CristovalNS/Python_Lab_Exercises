user_matrix = eval(input("Please enter a matrix: "))

print("Original matrix: ")
for a in range(len(user_matrix)):
    print(user_matrix[a])
print("*" * 20)

matrix = []

for y in range(len(user_matrix[0])):
    new_matrix = []
    for x in user_matrix:
        new_matrix.append(x[y])

    matrix.append(new_matrix)

print("Transposed matrix: ")
for b in range(len(matrix)):
    print(matrix[b])
