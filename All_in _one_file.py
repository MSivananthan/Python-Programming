Here's the optimized version of each script:

### Armstrong.py
```python
def is_armstrong_number(num):
    result = sum(int(digit) ** len(str(num)) for digit in str(num))
    return result == num

print(is_armstrong_number(int(input())))
```

### Average_of_Numbers.py
```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

print(calculate_average(list(map(int, input().split()))))
```

### Celsius_to_Fahrenheit.py
```python
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(celsius_to_fahrenheit(float(input())))
```

### Factorial.py
```python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(int(input())))
```

### Fibonacci.py
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(int(input()))
```

### Num_odd_even.py
```python
def is_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(is_even_or_odd(int(input())))
```

### Perfect_square.py
```python
import math

def is_perfect_square(num):
    return math.isqrt(num) ** 2 == num

print(is_perfect_square(int(input())))
```

### Prime_Factor.py
```python
def prime_factors(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(int(input())))
```

### Prime_Number_in_given_range.py
```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

print(primes_in_range(int(input()), int(input())))
```

### Prime_number.py
```python
def is_prime(num):
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

print(is_prime(int(input())))
```

### Reverse.py
```python
def reverse_string(s):
    return s[::-1]

print(reverse_string(input()))
```

### greatest_of_three_numbers.py
```python
def greatest_of_three(a, b, c):
    return max(a, b, c)

print(greatest_of_three(int(input()), int(input()), int(input())))
```

### palindrome.py
```python
def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

print(is_palindrome(int(input())))
```

### swap.py
```python
def swap(a, b):
    return b, a

print(swap(int(input()), int(input())))
```

These scripts are further optimized for conciseness and efficiency while maintaining clarity.
