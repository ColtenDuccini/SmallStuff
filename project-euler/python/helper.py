#general python function i made
import string, random

def is_palindrome(string):
    return string == string[::-1]

def get_nonunique(data):
    return list(filter(lambda x: data.count(x) > 1, data))

def get_digits(number):
    return list([int(x) for x in str(number)])

def roll_dice(rolls, sides):
    return [random.randint(1,sides) for i in xrange(rolls)]

def fib(n):
    x = 0
    y = 1
    while y < n:
        x, y = y, x + y
        yield y

def fib2(n):
    x = 0
    y = 1 
    counter = 0
    while counter < n:
        x, y = y, x + y
        yield y
        counter += 1
        
def amicable(a, b):
    return (sum_divisors(a) == b and sum_divisors(b) == a)

def get_divisors(n):
    return list(filter(lambda x: n % x == 0, range(1, n//2 + 1)))

def sum_divisors(n):
    sum = 0
    for i in range(1, n/2 + 1):
        if n % i == 0:
            sum += i
    return sum

def num_divisors(n): #taken from Jason's Coding Blog
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

def is_perfect(n):
    return sum_divisors(n) == n

def is_deficient(n):
    return sum_divisors(n) < n

def is_abundant(n):
    return sum_divisors(n) > n

def prime_factors(n):
    factors = []
    while n > 1:
        d = 2
        while (n % d != 0):
            d += 1
        factors.append(d)
        n = n // d
    return factors

def divisible_by_list(n, l):
    for x in l:
        if n % x != 0:
            return False
    return True

def makeMods(s): #based on TDWTF: The Mod Out System
    d = []
    for x in n.split(','):
        if '-' in x:
            i = x.index('-')
            left = int(x[:i])
            right = int(x[i+1:])
            d += range(left, right+1)
        else:
            d.append(int(x))
    return d
            
def fallTime(height): #freefall time on Earth 
    return ((2 * height)/9.8) ** 0.5

def carryCipher(cleartext): 
    alphabet = ' ' + string.uppercase
    ciphertext = ''
    addSum = 0
    for letter in cleartext.upper():
        index = alphabet.index(letter)
        addSum += index
        ciphertext += alphabet[(index + addSum) % 27]
    return ciphertext

def isPrime(n):
    if (n == 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    for i in xrange(3,int((n ** 0.5) + 1),2):
        if (n % i == 0):
            return False
    return True

def bad_primes_lister(n): #get the first n primes. naive method
    numbers = []
    i = 2
    while len(numbers) < n:
        if isPrime(i):
            numbers.append(i)
        i += 1
    return numbers

def sieve_of_eratosthenes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def get_neighbor_values(grid, x, y):
    neighbors = []
    if (y - 1 >= 0):
        neighbors.append(grid[x][y-1])
    if (y + 1 < len(grid[x])):
        neighbors.append(grid[x][y+1])
    if (x - 1 >= 0):
        neighbors.append(grid[x-1][y])
        if (y - 1 >= 0):
            neighbors.append(grid[x-1][y-1])
        if (y + 1 < len(grid[x])):
            neighbors.append(grid[x-1][y+1])
    if (x + 1 < len(grid)):
        neighbors.append(grid[x+1][y])
        if (y - 1 >= 0):
            neighbors.append(grid[x+1][y-1])
        if (y + 1 < len(grid[x])):
            neighbors.append(grid[x+1][y+1])
    return neighbors

def get_rotations(n):
    rotations = []
    m = str(n)
    l = len(m) - 1
    for i in range(len(m)):
        m = m[-1] + m[:l]
        rotations.append(m)
    return rotations

def all_rotations_prime(n):
    rotations = [int(x) for x in get_rotations(n)]
    return (False not in [isPrime(x) for x in rotations])

def spiral_sum(n):
    sums = 1
    m = 1
    delta = 2
    current = 3
    while (current <= (n ** 2)):
        sums += current
        if (m % 4 == 0):
            delta += 2
        current += delta
        m += 1
    return sums

def partial_triangle_sums(row1, row2):
    #row2 must be one element longer than row1
    out_row = []
    for i in range(len(row1)):
        n = row1[i]
        j, k = row2[i], row2[i+1]
        out_row.append(n + max((j, k)))
    return out_row
    
def best_tree_route(t):
    start_row = partial_triangle_sums(t[1],t[0])
    for i in range(2,len(t)):
        start_row = partial_triangle_sums(t[i],start_row)
    return start_row[0]

def truncations(s, right=True):
    s = str(s)
    truncs = []
    if right:
        while (s != ''):
            truncs.append(s)
            s = s[:-1]
    else:
        while (s != ''):
            truncs.append(s)
            s = s[1:]
    return truncs

def all_truncations_prime(n):
    truncs = truncations(n, True) + truncations(n, False)
    return (False not in [isPrime(int(x)) for x in truncs])

def gcd(a, b):
    while (a != b):
        if a > b:
            a -= b
        else:
            b -= a
    return a
    

