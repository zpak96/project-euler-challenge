
# ProjectEuler100 challenge - Problem 1
# Zane Paksi

# Question:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def main():
    # List comprehensions are quick, and easy to sum, so that will be my approach

    # creating list of int from 1-1000, then adding the conditional
    # of checking if i is a multiple of 3 or 5
    nums = [i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]

    # nums = a list of integers that are multiples of 3 or 5. Now we sum the list to produce the answer.
    answer = sum(nums)

    # nums could have been summed on the same line, but I'm adding the 'answer' to show a semblance of my thoughts.

    # An easier- but less elegant way to solve this problem is below!
    # answer = 0
    # for i in range(1, 1000):
    #     if i % 3 == 0 or i % 5 == 0:
    #         answer += i


main()
