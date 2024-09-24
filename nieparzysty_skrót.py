# Task 3, 2024

def get_last_digit(number):
    for i in range(10):
        if (number - i) % 10 == 0:
            return i


def odd_short(number):
    while True:
        if number < 1:
            break
        if number % 2 != 0:
            yield get_last_digit(number)
        number = (number - get_last_digit(number)) / 10


def get_odd_short(number):
    collection = list(odd_short(number))
    if len(collection) == 0:
        return None
    result = 0
    for i in range(len(collection)):
        result += (10).__pow__(i) * collection[i]
    return result


def get_non_odd_shorts(lines):
    for i in lines:
        if get_odd_short(int(i)) is None:
            yield int(i)


def get_divisors(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i


def get_common_divisors(number1, number2):
    for i in get_divisors(number1):
        if i in get_divisors(number2):
            yield i


def get_3_point_3(lines):
    for i in lines:
        lin = sorted(get_common_divisors(int(i), get_odd_short(int(i))), reverse=True)
        if len(lin) == 0:
            continue
        if lin[0] == 7:
            yield int(i)


def main():
    # 3.2
    print(sorted(get_non_odd_shorts(open("skrot_przyklad.txt", "r").readlines()), reverse=True))
    # 3.3
    print(list(get_3_point_3(open("skrot2_przyklad.txt", "r").readlines())))


if __name__ == '__main__':
    main()
