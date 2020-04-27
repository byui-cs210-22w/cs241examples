#!/usr/bin/python3

import random

def reseed_random(seed):
    ''' Use the seed to set RNG state and generate 10 values, but reseed
        on each loop to demonstrate how seed works '''
    for i in range(10):
        random.seed(seed)
        print(random.randint(1, 100), end=' ')
    else:
        print()

def sequence_random(seed):
    ''' Use the seed to set RNG state and generate 10 values, don't reseed
        on each loop to demonstrate how seed works '''
    random.seed(seed)
    for i in range(10):
        print(random.randint(1, 100), end=' ')
    else:
        print()

if __name__ == "__main__":
    seed = input("Enter a seed for this round, and 'stop' to quit: ")
    while seed != 'stop':
        reseed_random(seed)
        sequence_random(seed)
        print()
        seed = input("Enter a seed for this round, and 'stop' to quit: ")

