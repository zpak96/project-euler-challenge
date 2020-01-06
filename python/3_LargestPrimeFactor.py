
# ProjectEuler100 challenge - Problem 3
# Zane Paksi

# Question:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def main(n):

    d = 5
    while n > 1:
        while n % d == 0:
            n /= d
        if n < 1:
            break
        else:
            d = d + 1
    print(d-1)


main(600851475143)


