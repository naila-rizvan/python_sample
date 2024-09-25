
def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

def is_prime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
    else:
        return True

numbers = [4,7,3,9,3,7,1,6]
even_numbers = list(filter(is_even,numbers))
odd_numbers = set(filter(lambda x : x%2!=0,numbers))
prime_numbers = []

for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)

print("Even numbers are: ")
print(even_numbers)
print("Odd numbers are: ")
print(odd_numbers)
print("Prime numbers are: ")
print(prime_numbers)
