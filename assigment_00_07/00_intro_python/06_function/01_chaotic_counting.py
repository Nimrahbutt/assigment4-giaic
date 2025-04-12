import random

# Likelihood of stopping early
DONE_LIKELIHOOD = 0.2  # 20% chance to stop at each number

def done():
    """Returns True based on DONE_LIKELIHOOD chance"""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):  # Count from 1 to 10
        if done():
            return  # Stop counting early
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main()
