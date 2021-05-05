"""
ask the user for an integer, determines if it is a prime number
then list all prime number for 0 to 100 with a dict comprehension
"""


def is_prime(n):
    """Return True is the input nb is prime"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    while True:
        try:
            user_nb = int(input('Please enter a positive integer: '))
            break
        except:
            print('This is not an integer... try again.')
    if is_prime(user_nb):
        print(f'{user_nb} is a prime number')
    else:
        print(f'{user_nb} is NOT a prime number')

    primes = {p for p in range(100) if is_prime(p)}
    print(f'All prime numbers: {primes}')


if __name__ == "__main__":
    main()

