'''#Challenge 1: Counting Money!
Problem statement:#
Given an infinite number of quarters (25 cents), dimes (10 cents)
, nickels (5 cents), and pennies (1 cent), implement a function to calculate the minimum number of coins to represent v cents.

Input#
A variable v (total money to convert to coins) and a list of available coins

Output#
The minimum number of coins among the available coins that add up to the original number v, i.e., the coins represent v cents

Sample input#
v = 19
available_coins = [1, 5, 10, 25]
The available coins are in the ascending order.

Sample output#
result = [10, 5, 1, 1, 1, 1]
'''
v = int(input("Enter amount: "))
result = []
while v > 0:
    if v >= 25:
        v -= 25
        result.append(25)
    elif 25 > v >= 10:
        v -= 10
        result.append(10)
    elif 10 > v >= 5:
        v -= 5
        result.append(5)
    else:
        result.extend([1]*v)
        v -= v

print(result)

'''#Challenge 2: Connecting n Pipes with Minimum Cost
Problem statement#
Implement a function that connects n pipes of different lengths, into one pipe.
You can assume that the cost to connect two pipes is equal to the sum of their lengths.
We need to connect the pipes with minimum cost.

Input#
A list containing lengths of n pipes

Output#
The total cost of connecting the pipes

Sample input#
pipes = [4, 3, 2, 6]

Sample output#
result = 29
'''
'''#Challenge 3: Find the Egyptian Fraction's Denominators
Problem statement#
Every positive fraction can be represented as the sum of its unique unit fractions.
A fraction is a unit fraction, if the numerator is 1 and the denominator is a positive integer.
For example, 1/3 is a unit fraction. Such a representation is called an Egyptian Fraction.

Input#
Two variables numerator and denominator

Output#
A list in the format [d1, d2, ..., dn]

Sample input#
numerator = 2
denominator = 3

Sample output#
result = [2, 6]

Examples:
Egyptian Fraction Representation of 2/3 is 1/2 + 1/6
Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156
'''

