def get_divisors(number):
    for i in range(1, number):
        if number % i == 0:
            yield i


def is_prime(number):
    return len(list(get_divisors(number))) == 1


def get_prime_divisors(number):
    return list(filter(is_prime, get_divisors(number)))


def split_to_prime_divisors(number):
    prime_divisors = get_prime_divisors(number)
    result = 1
    break_signal = False
    while True:
        for i in prime_divisors:
            if result == number:
                break_signal = True
                break
            result = result * i
            yield i
        if break_signal:
            break


def main():
    number = int(input("Wprowadż liczbę: "))
    print("Jej dzielnikami pierwszymi są: ")
    for i in split_to_prime_divisors(number):
        print(i)


if __name__ == '__main__':
    main()
