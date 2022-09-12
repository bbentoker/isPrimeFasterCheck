import prime

isSame = True

for i in range(1, 10_000):
    if prime.isPrimeMyMethod(i) != prime.isPrime(i):
        isSame = False
        break

print("Is result the same:",isSame)