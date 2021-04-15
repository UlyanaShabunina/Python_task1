def maximum(a):
    i_max = 0
    for i in range(len(a)):
        if a[i] > a[i_max]:
            i_max = i
    return i_max

def minimum(a):
    i_min = 0
    for i in range(len(a)):
        if a[i] <= a[i_min]:
            i_min = i
    return i_min

def reverse(a, first_max, last_min):
    f_idx, l_idx = (first_max, last_min) if first_max < last_min else (last_min, first_max)
    part = a[f_idx + 1: l_idx]
    part.reverse()

    for i in range(f_idx + 1, l_idx):
        a[i] = part[i - f_idx - 1]
    return a


if __name__ == '__main__':
    a1 = [int(i) for i in input("Enter the list members separated by a space: ").split()]
    print("Default: ", a1)
    first_max = maximum(a1)
    last_min = minimum(a1)


    print("Result: ", reverse(a1, first_max, last_min))