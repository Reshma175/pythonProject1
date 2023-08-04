
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find(limit):
    primes = []
    for num in range(2, limit + 1):
        if prime(num):
            primes.append(num)
    return primes


prime_no = find(50)

print(prime_no)