import tilearn

x = [[1, 3, 5, 4, 7], [2, 3, 6, 3, 7], [3, 6, 3, 6, 8], [4, 2, 1, 6, 3], [5, 3, 5, 4, 7], [6, 3, 6, 3, 7], [7, 6, 3, 6, 8], [8, 2, 1, 6, 3], [9, 10, 3, 6, 8]]

# print(tilearn.show_mytime(x, 30))

scheduling = tilearn.show_mytime(x, 30)

for row in scheduling:
    print(row)