#---------------------------------------------
# Factorial - example of recursion
#---------------------------------------------
def factorial(n):
    
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#---------------------------------------------
# Exponent - recursion
#---------------------------------------------
def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        return base * exponent_calc(base,expo-1)

#Test: should print 125
b = 5
e = 3
print("exponent_calc(",b,",",e,") =", exponent_calc(b, e))


#---------------------------------------------
# Countdown - two ways - recursion and not
#---------------------------------------------

def count_down(start): # tail recursion
    # if we've reached 0 already, print 0 but do not call
    # another copy
    if start <= 0:
        print(start)
    
    # if we haven't reached 0 yet, print the current number,
    # then call count_down with the current number minus 1.
    else:
        print(start)
        count_down(start - 1)

def count_down4(start): # head recursion
    if start <= 0:
        print(start)
    else:
        count_down4(start - 1)
        print(start)

def count_down2(start): # without recursion
    print(start)
    for i in reversed(range(start)):
        print(i)

def count_down3(start): # without recursion or python functions
    while start >= 0:
        print(start)
        start -= 1
# Test
count_down4(5)
count_down3(6)

#---------------------------------------------
# Fibonacci - build a dictionary as you go
#---------------------------------------------
solved_already={} # store fibs that we solve along the way
def fib(n):
    # should check that n is positive integer here...
    if n in solved_already:
        return solved_already[n] # avoid re-calculating in recursion
    
    if n == 1 or n == 2:
        result = 1
    else:
        result =  fib(n - 1) + fib(n - 2)
    solved_already[n]=result
    return result

# Test
for n in range(1,11):
    print("fib(", n ,") =", fib(n))

