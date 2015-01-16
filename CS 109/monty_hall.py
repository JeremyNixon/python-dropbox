import numpy as np
# CS 109 Solution to HW0

def simulate_prizedoor(nsim):
    return np.random.randint(0, 3, (nsim))

def simulate_guess(nsim):
    return np.zeros(nsim, dtype=np.int)

def goat_door(prizedoors, guesses):
    
    #strategy: generate random answers, and
    #keep updating until they satisfy the rule
    #that they aren't a prizedoor or a guess
    result = np.random.randint(0, 3, prizedoors.size)
    while True:
        bad = (result == prizedoors) | (result == guesses)
        if not bad.any():
            return result
        result[bad] = np.random.randint(0, 3, bad.sum())

def switch_guess(guesses, goatdoors):
    result = np.zeros(guesses.size)
    switch = {(0, 1): 2, (0, 2): 1, (1, 0): 2, (1, 2): 0, (2, 0): 1, (2, 1): 0}
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            mask = (guesses == i) & (goatdoors == j)
            if not mask.any():
                continue
            result = np.where(mask, np.ones_like(result) * switch[(i, j)], result)
    return result

def win_percentage(guesses, prizedoors):
    return 100 * (guesses == prizedoors).mean()

nsim = 1000000

#keep guesses
print "Win percentage when keeping original door"
print win_percentage(simulate_prizedoor(nsim), simulate_guess(nsim))

#switch
pd = simulate_prizedoor(nsim)
guess = simulate_guess(nsim)
goats = goat_door(pd, guess)
guess = switch_guess(guess, goats)
print "Win percentage when switching doors"
print win_percentage(pd, guess).mean()

