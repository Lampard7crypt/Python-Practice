def is_prime(number):
    if number < 3:
        return True if number == 1 else False
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))