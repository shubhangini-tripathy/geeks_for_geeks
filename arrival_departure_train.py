train_times = [(9.0, 9.10), (9.40, 12.0), (9.50, 11.20),
               (11.0, 11.30), (15.0, 19.0), (18.0, 20.0)]
train_times.sort()
count = 0
train_list = []

for train_time in train_times:
    train_list = list(filter(lambda x: x[1] > train_time[0], train_list))
    train_list.append(train_time)
    count = max(count, len(train_list))
print(count)
