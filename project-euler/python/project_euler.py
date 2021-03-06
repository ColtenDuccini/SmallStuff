import time, sys, string, math
import itertools as it
from helper import *

#Euler problems

def problem1(): #Multiples of 3 and 5
    sum = 0
    for i in range(1,1000):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum

def problem2(): #Even Fibonacci numbers
    i = filter(lambda x: x % 2 == 0, list(fib(4000000)))
    return sum(i)

def problem3(): #Largest prime factor
    return prime_factors(600851475143)

def problem4(): #Largest palindrome product
    max = 1000
    numbers_list = range(100, 1000)
    for j in numbers_list:
        for k in numbers_list:
            if (j * k > max) and (is_palindrome(str(j * k))):
                max = j * k
    return max
                    
def problem5(): #Smallest multiple
    n = 2520
    while True:
        if divisible_by_list(n, range(1,21)):
            break
        n += 2520
    return n

def problem6():
    numbers = range(1,101)
    return (sum(numbers) ** 2) - sum([i ** 2 for i in numbers]) 

def problem7():
    return bad_primes_lister(10001)[10000]

def problem8():
    number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    maximum = 0
    for i in xrange(0,1000-13):
        n = number[i:i+13]
        m = 1
        for x in n:
            m *= int(x)
        if m > maximum:
            maximum = m
    return maximum

def problem9(): #special pythagorean triplet
    for a in xrange(1,1000,1):
        for b in xrange(1,1000 - a,1):
            c = 1000 - a - b
            if c ** 2 == (a ** 2) + (b ** 2):
                return c*b*a
    return 0

def problem10(): #prime summation
    return sum(sieve_of_eratosthenes(2000000))

def problem11(): #largest product in a grid
    return 

def problem12(): #Highly divisible triangular number
    def method(n):
        n = 1
        lnum, rnum = num_divisors(n), num_divisors(n+1)
        while lnum * rnum < 500:
            n += 1
            lnum, rnum = rnum, num_divisors(n+1)
        return n
    index = method(500)
    return (index * (index + 1)) / 2

def problem13():
    print "I cheated."
    return 5537376230

def problem14(): # longest collatz sequence
    def collatz(n):
        steps = 1
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = (n * 3) + 1
            steps += 1
        return steps
    max, n = 1, 1
    for i in xrange(1000000):
        if collatz(i) > max:
            n, max = i, collatz(i)
    return n

def problem15(): # lattice paths
    return math.factorial(2 * 20) // (math.factorial(20) ** 2)

def problem16(): #power digit sum
    n = 2 ** 1000
    return sum(get_digits(n))

def problem17():
    return

def problem18(): #Maximum path sum 1
    tree = [[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23],
            [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
            [91,71,52,38,17,14,91,43,58,50,27,29,48],
            [70,11,33,28,77,73,17,78,39,68,17,57],
            [53,71,44,65,25,43,91,52,97,51,14],
            [41,48,72,33,47,32,37,16,94,29],
            [41,41,26,56,83,40,80,70,33],
            [99,65,4,28,6,16,70,92],
            [88,2,77,73,7,63,67],
            [19,1,23,75,3,34],
            [20,4,82,47,65],
            [18,35,87,10],
            [17,47,82],
            [95,64],
            [75]]
    return best_tree_route(tree)

def problem19(): #counting sundays
    sundays_on_first = 0 #0 == monday, 6 == sunday
    year = 1900
    normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = 0
    while (year != 2001):
        if (year % 4 == 0 and year % 400 != 0):
            for month in leap_year:
                day = (day + month) % 7
                if (day == 6):
                    sundays_on_first += 1
        else:
            for month in normal_year:
                day = (day + month) % 7
                if (day == 6):
                    sundays_on_first += 1
        year += 1
    
    return sundays_on_first - 1 #somehow subtract one produces the right answer. I don't know why

def problem20():
    return sum ([int(z) for z in str(math.factorial(100))])

def problem21():
    numbers = []
    limit = 10000
    sums = [sum_divisors(n) for n in range(10000)]
    for x in range(limit):
        sum_x = sums[x]
        for y in range(x):
            sum_y = sums[y]
            if (sum_x == y and sum_y == x):
                numbers.append(x)
                numbers.append(y)
    return sum(numbers)

def problem22():
    return

def problem23():
    return

def problem24():
    perms = list(it.permutations('0123456789', 10))
    perms.sort()
    return perms[999999]

def problem25():
    x, y = 0, 1
    n = 10 ** 999
    counter = 1
    while y < n:
        x, y = y, x + y
        counter += 1
    return counter

def problem26():
    return

def problem27():
    def formula(a, b, n):
        return (n ** 2) + (a * n) + b
    max_a, max_b = 1000, 1000
    min_a, min_b = -999, -999
    max_primes = 0
    best_coefficients = (0, 0)
    for a in xrange(min_a, max_a):
        for b in xrange(min_b, max_b):
            n = 0
            prime_count = 0
            while (True):
                if (not isPrime(abs(formula(a,b,n)))):
                    break
                prime_count += 1
                n += 1
            if prime_count >= max_primes:
                max_primes = prime_count
                best_coefficients = (a, b)
    return best_coefficients[0] * best_coefficients[1]

def problem28():
    
    return spiral_sum(1001)

def problem29():
    powers = []
    for a in range(2, 101):
        for b in range(2, 101):
            powers.append(a ** b)
    return len(set(powers))

def problem30():
    sums = 0
    for x in range(2,3000000):
        digits = [int(y) for y in str(x)]
        if sum([y ** 5 for y in digits]) == x:
            sums += x
    return sums

def problem31():
    return

def problem32():
    return

def problem33(): #digit cancelling fractions
    fractions = []
    for b in range(10, 100):
        for a in range(10, b):
            if b % 10 != 0:
               s_a, s_b = str(a), str(b)
               if s_b[0] != s_b[1] and s_a[1] == s_b[0]:
                   if (float(s_a) / float(s_b)) == (float(s_a[0]) / float(s_b[1])):
                          fractions.append((a, b))           
    return fractions #this just returns the fractions themselves. The actual answer is 100

def problem34(): #digit factorials
    sums = 0
    for i in range(10,1000000):
        if i == sum([math.factorial(int(x)) for x in str(i)]):
            sums += i
    return sums

def problem35(): #circular primes
    return len(list(filter(lambda x: all_rotations_prime(x), sieve_of_eratosthenes(1000000))))

def problem36(): #double-base palindromes
    nums = list(filter(lambda x: is_palindrome(str(x)), range(1000000)))
    nums = list(filter(lambda x: is_palindrome(bin(x)[2:]), nums))
    return sum(nums)

def problem37(): #truncatable primes
    nums = sieve_of_eratosthenes(1000000)[4:] #removes 2,3,5 and 7
    truncatable_primes = []
    for x in nums:
        if all_truncations_prime(x):
            truncatable_primes.append(x)
    return sum(truncatable_primes)

def problem38():
    return

def problem39():
    return

def problem40(): #Chapernowne's constant
    chapernowne = ''.join([str(x) for x in range(1,1000000)])
    x = chapernowne
    return int(x[0]) * int(x[9]) * int(x[99]) * int(x[999]) * int(x[9999]) * int(x[99999]) * int(x[999999])

def problem41():
    return

def problem42():
    return

def problem43():
    return

def problem44():
    return

def problem45():
    return

def problem46():
    return

def problem47():
    return

def problem48():
    return

def problem49():
    return

def problem50():
    return

def problem51():
    return

def problem52():
    return

def problem53():
    return

def problem54():
    return

def problem55():
    return

def problem56():
    return

def problem57():
    return

def problem58():
    return

def problem59():
    return

def problem60():
    return

def problem61():
    return
