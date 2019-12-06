def reverse(text):
    n = len(text)

    if n == 0:
        return text

    return text[n-1] + reverse(text[:n-1])


print(reverse('python'))
