
# ProjectEuler100 challenge - Problem 2
# Zane Paksi

# Question:
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def fib(a, b, answer):
    c = a + b

    # if c is less than 4 million, check if it is even, then call fib again,
    # but this time use b in place of a, and c in place of b.
    if c < 4000000:
        # only worrying about even numbers
        if c % 2 == 0:
            answer += c
        fib(b, c, answer)
    else:
        # answer is found here
        print(answer)


def main():
    num1 = 1
    num2 = 2

    answer = num2

    # call fib to create fibonacci sequence
    fib(num1, num2, answer)


main()
