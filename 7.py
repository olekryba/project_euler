
def is_prime(tal, primes):
    if tal <= 1:
        return False
    for prime in primes:
        if tal % prime == 0: 
            return False
    return True

primes = [2]
tal = 1
while len(primes) < 10001:
    if is_prime(tal, primes):
        primes.append(tal)
    tal += 1


print(primes)