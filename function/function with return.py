def add(a, b):

    return a + b


def is_true(a):

    return bool(a)



res = add(2, 3)
print("Result of add function is {}".format(res))

res = is_true(2 < 5)
print("\nResult of is_true function is {}".format(res))