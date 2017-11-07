def get_possible_way(m):
    if m < 0:
        return 0
    if m == 0:
        return 1
    return get_possible_way(m - 1) + get_possible_way(m - 2) + get_possible_way(m - 3)


N = 3
print(get_possible_way(N))
