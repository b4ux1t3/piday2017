"""
This is just a way to see which method alluded to in the README will produce the
best result.

Think of it as a test, I guess.
"""
import randompi
import statistics
import time

print("Starting timer")

start_time = time.time()

# Basically, I'm going to make a bunch of lists holding a thousand (1000) of values of pi as
# calculated via various parameters.

# Baseline, method works as shown in the original video.
# Iterations = 500
# Max random value = 120
baseline = [randompi.run_calculation(501, max_random_number=121) for i in range(1000)]

baseline_average = statistics.mean(baseline)

print("                    Baseline average estimation for pi:\t{}".format(baseline_average))
print("                                        Execution time:\t{}".format(time.time() - start_time))
elapsed_time = time.time()

#Baseline, but done a million times
# Iterations = 1000000
# Max random value = 120
million_baseline = [randompi.run_calculation(1000001, max_random_number=121) for i in range(1000)]

million_baseline_average = statistics.mean(million_baseline)

print("            Million baseline average estimation for pi:\t{}".format(million_baseline_average))
print("                                        Execution time:\t{}".format(time.time() - elapsed_time))
elapsed_time = time.time()

# Iterations = 500
# Default max value (sys.maxsize)
baseline_max_value = [randompi.run_calculation(501) for i in range(1000)]

baseline_max_value_average = statistics.mean(baseline_max_value)

print("      500 tries at max value average estimation for pi:\t{}".format(baseline_max_value_average))
print("                                        Execution time:\t{}".format(time.time() - elapsed_time))
elapsed_time = time.time()

# Iterations = 1000000
# Default max value (sys.maxsize)
million_max_value = [randompi.run_calculation(1000001) for i in range(1000)]

million_max_value_average = statistics.mean(million_max_value)

print("A million tries at max value average estimation for pi:\t{}".format(million_max_value_average))
print("                                        Execution time:\t{}".format(time.time() - elapsed_time))
elapsed_time = time.time()
