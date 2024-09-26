from multipledispatch import dispatch

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

@dispatch()
def sum(a:int,b:int):
    return a+b

@dispatch()
def sum(a:int,b:int,c:int):
    return a+b+c

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

print("--------------------------------")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum: " + str(sum(num1,num2)))

num3 = int(input("Enter third number: "))
print("Sum: " + str(sum(num1,num2,num3)))
