import time

def isPrimeMyMethod(number):
    for i in range(2, number):
        if pow(i, 2) > number:
            break
        if number % i == 0:
            return False
    return True

#Some function I got from the web
def isPrime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def checkTime():

    start = time.time()
    firstMethodTime = 0
    secondMethodTime = 0

    for i in range(2, 100_000):
        isPrimeMyMethod(i)

    firstMethodTime = time.time() - start

    start = time.time()

    for i in range(2, 100_000):
        isPrime(i)

    secondMethodTime = time.time() - start

    print("My method took: " + str(firstMethodTime))
    print("The other method took: " + str(secondMethodTime))

if __name__ == '__main__':
    checkTime()
