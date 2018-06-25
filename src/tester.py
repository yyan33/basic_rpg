from itertools import chain

x = [[1, 2, 3, 4], [5], [6, 7]]

for i in range(len(x)):
    for j in range(len(x[i])):
        # print("i: {} j: {}".format(i,j))
        print(x[i][j])
