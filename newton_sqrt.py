import math

def newton_sqrt(number, guess, tolerance):
    """
        Newton–Raphson method - Root-finding algorithm.
    """
    while True:
        sqrt = (guess + number/guess) / 2
        if abs(sqrt - guess) < tolerance:
            break
        guess = sqrt
    return sqrt

# Test 1
number = 1.0
r1 = newton_sqrt(number, 1, 1e-7)
r2 = math.sqrt(number)
diff = abs(r1 - r2)
print('number: ', number)
print('newton_sqrt(number): ', r1)
print('math.sqrt(number): ', r2)
print('Difference: ', diff)
print('\n')

# Test 2
number = 2.0
r1 = newton_sqrt(number, 1, 1e-7)
r2 = math.sqrt(number)
diff = abs(r1 - r2)
print('number: ', number)
print('newton_sqrt(number): ', r1)
print('math.sqrt(number): ', r2)
print('Difference: ', diff)
print('\n')

# Test 3
number = 144
r1 = newton_sqrt(number, 1, 1e-7)
r2 = math.sqrt(number)
diff = abs(r1 - r2)
print('number: ', number)
print('newton_sqrt(number): ', r1)
print('math.sqrt(number): ', r2)
print('Difference: ', diff)
    
