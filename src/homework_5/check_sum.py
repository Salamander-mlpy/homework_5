import random

# 1. Primality checker function
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# 2. Prime numbers list generation function
def primes(count: int) -> list[int]:
    prime_list = []
    num = 2
    while len(prime_list) < count:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

# 3. Checksum calculation function
def checksum(x: list) -> int:
    checksum_value = 0
    for num in x:
        checksum_value = (checksum_value + num) * 113 % 10000007
    return checksum_value

# 4. Pipeline function that performs all required actions
def pipeline() -> int:
    # Generate the first 1000 prime numbers
    prime_list = primes(1000)

    # Shuffle the list using seed 100
    random.seed(100)
    random.shuffle(prime_list)

    # Calculate the checksum for the shuffled list
    checksum_value = checksum(prime_list)

    return checksum_value, prime_list

# 5. Main block to print the result
if __name__ == "__main__":
    checksum_result, prime_list = pipeline()
    #print("Checksum:", checksum_result)
    #print("Shuffled Prime List:", prime_list)
    print(prime_list)
