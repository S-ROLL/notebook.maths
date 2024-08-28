import tilearn

data = [['Job 1', 4, 0, 10, 1], ['Job 2', 9, 0, 10, 3], ['Job 3', 6, 0, 10, 2], ['Job 4', 7, 0, 10, 3], ['Job 5', 4, 0, 10, 2], ['Job 6', 5, 0, 10, 1], ['Job 7', 8, 0, 10, 3], ['Job 8', 3, 0, 10, 1], ['Job 9', 2, 0, 10, 1], ['Job 10', 6, 0, 10, 2]]

#print(tilearn.show_mytime(data, 10))

schedule = tilearn.show_mytime(data, 10)

for row in schedule:
    print(row)