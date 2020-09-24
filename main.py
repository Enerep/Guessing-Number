import time
import random as rand

# Starting the timer
start_time = time.time()

guess_num = int(input("Number between 1 to 1,000,000"))

random_nums = rand.sample(range(100000), 100000)
index = random_nums.index(guess_num)
execute_time = time.time() - start_time
print("It took {} seconds to guess: {}".format(execute_time, guess_num))

