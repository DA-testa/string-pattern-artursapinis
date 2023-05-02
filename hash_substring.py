def read_input():
    choice = input().rstrip()
    if choice == 'I':
        return input().rstrip(), input().rstrip()
    elif choice == 'F':
        with open('tests/06', 'r') as f:
            return f.readline().rstrip(), f.readline().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    x = 263
    p = 10 ** 9 + 7
    res = []
    tLength = len(text)
    pLength = len(pattern)
    if tLength < pLength:
        return res
    hp = pow(x, pLength - 1, p)
    pat = sum([ord(c) * pow(x, i, p) for i, c in enumerate(pattern)]) % p
    h = sum([ord(c) * pow(x, i, p) for i, c in enumerate(text[:pLength])]) % p
    if h == pat and text[:pLength] == pattern:
        res.append(0)
    for i in range(pLength, tLength):
        h = (h - ord(text[i - pLength]) * hp) % p
        h = (h * x + ord(text[i])) % p
        if h == pat and text[i - pLength + 1:i + 1] == pattern:
            res.append(i - pLength + 1)
    return res


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
