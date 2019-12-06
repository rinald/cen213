# len(a) <= len(b)
def count_substring(a, b):
    n = 0
    l1 = len(a)
    l2 = len(b)

    for i in range(l2-l1+1):
        if a == b[i:i+l1]:
            n += 1

    return n


if __name__ == '__main__':
    print(count_substring('ab', 'abcdabab'))
