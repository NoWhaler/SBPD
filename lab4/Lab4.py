import math


# Перша частина

def fast_discrete_potential(message, key, p):
    binary_key = bin(key).replace('0b', '')
    cipher_e = 1
    for i in range(len(binary_key)):
        cipher_e = ((cipher_e ** 2) * (message ** int(binary_key[i]))) % p
    return cipher_e


message = int(input('Input the message: '))
key = int(input('Input the public key: '))
p_parameter = int(input('Input P-parameter: '))

print('\nCipher E = ', fast_discrete_potential(message, key, p_parameter), '\n')


# Друга частина

def generation_prime_number(p_max, simple_small_number):
    k = math.ceil(math.log(p_max / 2, simple_small_number))
    p1 = 2 * (simple_small_number ** k) + 1
    p2 = 2 * (simple_small_number ** k) - 1
    if fast_discrete_potential(2, p1 - 1, p1) == 1:
        p = p1
    if fast_discrete_potential(2, p2 - 1, p2) == 1:
        p = p2
    else:
        while fast_discrete_potential(2, p1 - 1, p1) != 1:
            p1 += 2
        p = p1
    return p


def isprime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d


pMax = int(input('Input pmax: '))
simpleSmallNumber = int(input('Input small simple number: '))

if isprime(simpleSmallNumber) == simpleSmallNumber:
    print('\nPrime number P was generated: ', generation_prime_number(pMax, simpleSmallNumber))
else:
    print("\nThe small number entered is not prime. Try another one.")
