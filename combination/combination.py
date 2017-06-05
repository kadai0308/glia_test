# initialize
data_table = [[ -1 for i in range(34)] for j in range(991)]

# fill know data
for i in range(991):
    data_table[i][1] = i
for i in range(34):
    data_table[i][i] = 1


def cb(a, b):
    if b == 1:
        data_table[a][b] = a
        return a
    elif a == b:
        data_table[a][b] = 1
        return 1

    if data_table[a-1][b] != -1 and data_table[a-1][b-1]:
        print("1")
        return data_table[a-1][b] + data_table[a-1][b-1]

    elif data_table[a-1][b] != -1 and data_table[a-1][b-1] == -1:
        print("2")
        return data_table[a-1][b] + cb(a-1, b-1)

    elif data_table[a-1][b] == -1 and data_table[a-1][b-1] != -1:
        print("3")
        return data_table[a-1][b] + cb(a-1, b-1)

    else:
        print("4")
        return cb(a-1, b) + cb(a-1, b-1)

result = cb(990, 33)
