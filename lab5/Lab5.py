import math
import random


def fast_discrete_potential(message, key, p):
    binary_key = bin(key).replace('0b', '')
    cipher_e = 1
    for i in range(len(binary_key)):
        cipher_e = ((cipher_e ** 2) * (message ** int(binary_key[i]))) % p
    return cipher_e


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


p_max = int(input('Input P_max: '))
q_max = int(input('Input Q_max: '))
simple_small_number = int(input('Input small simple number: '))


if isprime(simple_small_number) != simple_small_number:
    print("\nThe small number entered is not prime. Try another one.")
else:
    p = generation_prime_number(p_max, simple_small_number)
    q = generation_prime_number(q_max, simple_small_number)
    print('\nGenerated simple number P = ', p)
    print('Generated simple number Q = ', q)

    encryption_parameter = p * q
    Euler_function = (p - 1) * (q - 1)

    public_key = random.randint(int(math.log(encryption_parameter, 2)), encryption_parameter)
    while math.gcd(public_key, Euler_function) != 1:
        public_key = random.randint(int(math.log(encryption_parameter, 2)), encryption_parameter)

    z = 1
    secret_key = z * Euler_function + 1
    while secret_key % public_key != 0:
        z += 1
        secret_key = z * Euler_function + 1
    secret_key /= public_key

    print('Encryption keys for the RSA system are specified in pairs:\n<Кс, Р> - private key <{0}, {2}>\n'
          '<Ко, Р> - public key <{1}, {2}>'.format(int(secret_key), public_key, encryption_parameter))

    s = int(input('Input S: '))
    e = fast_discrete_potential(s, int(public_key), encryption_parameter)
    s = fast_discrete_potential(e, int(secret_key), encryption_parameter)
    print('The decryption was successful. The cipher E = {0} corresponds to the original message S = {1}'.format(e, s))
