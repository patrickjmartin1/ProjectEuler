from math import sqrt, ceil, floor


def main_func():
    max_squared = 1929394959697989990
    min_squared = 1020304050607080900

    max_limit = ceil(sqrt(max_squared) / 10)
    min_limit = floor(sqrt(min_squared) / 10)

    print(min_limit, max_limit)

    print(max_limit - min_limit)

    print(pow(max_limit, 2))

    print(pattern_match(min_squared+1))

    for n in range(max_limit, min_limit, -1):
        # print((n - min_limit)/(max_limit - min_limit))
        n2 = pow(n, 2)
        if pattern_match(n2):
            print("Found it: {}".format(str(n) + '0'))
            print(pow(int(str(n) + '0'), 2))
            break


def pattern_match(n):
    base_str = "23456789"
    n_str = str(n)
    n_str = n_str[2::2]
    for l1, l2 in zip(n_str, base_str):
        if l1 != l2:
            return False
    return True


if __name__ == "__main__":
    main_func()
    """
    This works: Feels a bit like cheating, but walking backwards was correct
    
    Correct answer: 1389019170
    """