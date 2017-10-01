def swap(elements, i, j):
    elements[i], elements[j] = elements[j], elements[i]


def reverse(elements, i, j):
    for offset in range((j - i + 1) // 2):
        swap(elements, i + offset, j - offset)


def next_permutation(elements):
    last_index = len(elements) - 1
    if last_index < 1:
        return

    i = last_index - 1
    while i >= 0 and elements[i] > elements[i + 1]:
        i -= 1

    # If there is no greater permutation, return to the first one.
    if i < 0:
        reverse(elements, 0, last_index)
    else:
        j = last_index
        while j > i + 1 and elements[j] < elements[i]:
            j -= 1

        swap(elements, i, j)
        reverse(elements, i + 1, last_index)

    return elements


def next_permutation_number(n):
    return to_number(next_permutation(to_digits(n)))


def to_digits(n):
    c = []
    for digit in str(n):
        c.append(int(digit))
    return c


def to_number(lst):
    return ''.join(str(digit) for digit in lst)


print(next_permutation_number(1234))
print(next_permutation_number(412653))
