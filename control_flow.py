# Take a integer
#
#x = int(input("Please enter an integer: "))
"""
x = 2
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x ==  0:
    print("Zero")
elif x == 1:
    print('Single')
else:
    print('More')

"""
"""
words = ['cat', 'windows', 'defenestrate']
print("Words ", "Length")
for w in words:
    print(w, len(w))


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i+1, a[i])
"""
"""
for n in range(2, 10):
    for x in range(2, n):
        if n%x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
"""
"""
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
"""
"""
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()

fib(2000)
"""
"""
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b

    return result

f100 = fib2(100)
print(f100)
"""

def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)

#ask_ok("Would you like to do it?")

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
#print(f(3))
#print(f(3))
#print(f(3))
args = [3, 6]
#print(list(range(*args)))

def parrot(voltage, state='a stiff', action='voom'):
    print("--- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts thorugh it.", end=" ")
    print("E's", state, "!")
d = {"voltage": "four million", "state":"bleedin' demised", "action": "VOOM"}
#parrot(**d)


def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(10)
#print(f(0))


for i in range(2, 10):
    for j in range(2, i):
        if i%j == 0:
            print(i, "equals", j, "*", i//j)
            break
        else:
            print(i, "yes")
            break














