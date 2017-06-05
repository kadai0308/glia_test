
data_table = [[ -1 for i in range(34)] for j in range(991)]

def cb(a, b):
    if b == 1:
        data_table[a][b] = a
        return a
    elif a == b:
        data_table[a][b] = 1
        return 1

    if data_table[a-1][b] != -1 and data_table[a-1][b-1]:
        return data_table[a-1][b] + data_table[a-1][b-1]

    elif data_table[a-1][b] != -1 and data_table[a-1][b-1] == -1:
        return data_table[a-1][b] + cb(a-1, b-1)

    elif data_table[a-1][b] == -1 and data_table[a-1][b-1] != -1:
        return data_table[a-1][b] + cb(a-1, b-1)

    else:
        return cb(a-1, b) + cb(a-1, b-1)

result = cb(990, 33)
