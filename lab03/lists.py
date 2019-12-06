a = [(1,), (1, 2), (1, 2, 3)]

print(a[1][1])  # 2nd element of 2nd element of a

b = [
    list(range(10)),
    list(range(10)),
    list(range(10)),
    list(range(10))
]

print(b[0][-2:])  # last 2 elements of the 1st element of b
