n = int(input('Enter Number '))

def get_prime_factors(n):
    factors = list()
    divisor = 2
    while(divisor <= n):
        if(n % divisor == 0):
            factors.append(divisor)
            n = n/divisor
        else:
            divisor += 1
    return factors

 
print(get_prime_factors(n))