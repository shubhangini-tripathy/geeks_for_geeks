# start = [3, 0, 5, 8, 5, 1]
# finish = [4, 6, 7, 9, 9, 2]
activity = [(3, 4), (0, 6), (5, 7), (8, 9), (5, 9), (1, 2)]
activity.sort(key=lambda x: (x[1], x[0]))
preve = activity[0][1]
print(activity[0])
for i in range(1,len(activity)):
    if activity[i][0] >= preve:
        print(activity[i])
        preve = activity[i][1]




    