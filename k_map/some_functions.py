import numpy as np

double = [["00", "01"],
          ["10", "11"]]
triple = [["000", "001", "011", "010"],
          ["100", "101", "111", "110"]]
quadruple = np.array([["0000", "0001", "0011", "0010"],
                     ["0100", "0101", "0111", "0110"],
                     ["1100", "1101", "1111", "1110"],
                     ["1000", "1001", "1011", "1010"]])
letters = ["w", "x", "y", "z"]

def create_dict(n):
    indexes = {}
    if n == 2:
        array = double
    elif n == 3:
        array = triple
    else:
        array = quadruple
    for i in range(len(array)):
        for j in range(len(array[0])):
            indexes[array[i][j]] = [i, j]
    return indexes

# user_input = input().split()

def numbers_to_circuit(user_input):
    circuit = []
    for i in user_input:
        new = ''
        for j in range(len(i)):

            if i[j] == "0":
                new += letters[j]
            elif i[j] == "-":
                continue
            else:
                new += f"~{letters[j]}"
        circuit.append(new)
    return circuit
# circuit = numbers_to_circuit(user_input)
# print(circuit)
def create_matrix(user_input):
    n = len(user_input[0])
    if n == 3:
        result = np.zeros((2, 4))
    else:
        result = np.zeros((n, n))
    d = create_dict(n)
    for i in user_input:
        x = d[i][0]
        y = d[i][1]
        result[x][y] = 1
    return result
# matrix = create_matrix(user_input)

def matrix_index(matrix):
    indexes =[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                indexes.append((i, j))
    return indexes
# ind = matrix_index(matrix)
# print(ind)

# print(matrix)


