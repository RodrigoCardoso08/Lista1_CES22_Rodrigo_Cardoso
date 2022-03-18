def is_prime(n):
    count_is_prime = 0
    for i in range(n):
        if i != 0 and i != 1 and n % i == 0 :
            count_is_prime = count_is_prime + 1
    if count_is_prime == 0:
        return True
    else:
        return False


