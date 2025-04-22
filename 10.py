def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
num = 2


while num < 2000000:
    if is_prime(num):
        primes.append(num)
    num += 1


sum_of_primes = sum(primes)

print(sum_of_primes)
