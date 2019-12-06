def count_substring(s1, s2):
    l1, l2 = len(s1), len(s2)

    i = 1 if s1 == s2[:l1] else 0

    if l1 == l2:
        return i
    else:
        return i + count_substring(s1, s2[1:])


print(count_substring('ab', 'abcdabab'))
