def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    elif n % i == 0:
        return False
    elif i*i > n:
        return True
    return is_prime(n, i+1)

def in_range(lb, ub):
    prime_list = []
    for i in range(lb, ub+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

lower_bound = int(input("Enter the lower bound : "))
upper_bound = int(input("Enter the upper bound : "))

prime_numbers = in_range(lower_bound, upper_bound)
print(" ")
print(f"The prime numbers between {lower_bound}, {upper_bound} is : ")
print(prime_numbers)

