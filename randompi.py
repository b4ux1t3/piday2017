import random
import math
import sys 
import fractions

coprimes = 0
cofactors = 0

for i in range(sys.maxsize):
    try:
        x = random.randint(1, 121)
        y = random.randint(1, 121)
        gcd = fractions.gcd(x, y)

        if gcd == 1:
            coprimes += 1
        else:
            cofactors += 1
        if i % 100000 == 0:
            print("Currently on {}".format(i))
    except KeyboardInterrupt:
        break

total = coprimes + cofactors
coprime_probability = coprimes / total
pi_estimate = math.sqrt(6/coprime_probability)

print()
print("        Total Tries:\t{}".format(total))
print("           Coprimes:\t{}".format(coprimes))
print("          Cofactors:\t{}".format(cofactors))
print("Coprime probability:\t{}".format(coprime_probability))
print("        Pi Estimate:\t{}".format(pi_estimate))