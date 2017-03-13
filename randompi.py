import random
import math
import sys 
import fractions

# run_calculation takes a number of iterations to perform and then runs that many
# random number coprime comparisons. It returns a value for pi, and will print
# out the results. It also optionally takes in a maximum random number, which defaults
# to sys.maxsize.
def run_calculation(iterations, max_random_number = sys.maxsize):

    coprimes = 0
    cofactors = 0

    for i in range(iterations):
        try:
            x , y = generate_two_numbers(max_random_number)
            
            gcd = fractions.gcd(x, y)

            if gcd == 1:
                coprimes += 1
            else:
                cofactors += 1

            #report what number we're on every 100000 iterations
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

    return pi_estimate

def generate_two_numbers(max_random_number):
    return (random.randint(1, max_random_number), random.randint(1, max_random_number))

def main():
    run_calculation(sys.maxsize)

if __name__ == "__main__":
    main()