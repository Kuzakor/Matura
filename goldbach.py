def get_divisors(number):
    for i in range(1, number):
        if number % i == 0:
            yield i


def is_prime(number):
    return len(list(get_divisors(number))) == 1


def get_prime_numbers(limit):
    for i in range(limit):
        if is_prime(i):
            yield i


def possible_pairs(data):
    return [(a, b) for idx, a in enumerate(data) for b in data[idx + 1:]]


def is_goldbach(number):
    for i in possible_pairs(list(get_prime_numbers(number))):
        if sum(i) == number:
            return True
    return False

def main():
    num = 4
    while True:
        print(num, is_goldbach(num))
        num += 2


if __name__ == '__main__':
    main()
