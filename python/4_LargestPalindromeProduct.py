# ProjectEuler100 challenge - Problem 4
# Zane Paksi

# Question:
# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.


def checkPal(pal):
    if str(pal) == str(pal)[::-1]:
        return pal


def main():
    top = 999
    bot = 100
    pal = 0
    for x in range(top, bot, -1):
        for y in range(top, bot, -1):
            if checkPal(x*y) and x*y > pal:
                pal = x*y

    print(pal)


main()
