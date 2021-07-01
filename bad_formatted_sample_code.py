# list_primes.py
def is_prime(number):
  for i in range(2, number):
    if number % i == 0:
      return False
    return True


def list_primes(upper):
  for number in range(2, upper):
    if is_prime(number):
      print(f"{number} is prime")


list_primes(10)
