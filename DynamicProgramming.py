# Recursion
# Write a function to output Pascal's Triangle
# given the level

# 1:    1
# 2:   1 1
# 3:  1 2 1
# 4: 1 3 3 1

def pascalTriangle(level: int) -> list[list[int]]:
    answer = []
    if level == 1:
        return [[1]]
    elif level == 2:
        return [[1], [1, 1]]
    else:
        pass

# https://leetcode.com/problems/construct-the-rectangle/
# Resource: https://www.codechef.com/wiki/tutorial-dynamic-programming

# 0-1 Knapsack Problem
class knapsack:
    def solveKnapsack(self, profits: list[int], weights: list[int], capacity: int):
        return self.__knapsackRecursive(profits, weights, capacity, 0)

    def __knapsackRecursive(self, profits: list[int], weights: list[int], capacity: int, index: int):
        if capacity <= 0 or index >= len(profits): return 0

        choice1 = 0
        if weights[index] <= capacity:
            choice1 = profits[index] + self.__knapsackRecursive(profits, weights, capacity - weights[index], index + 1)
        choice2 = self.__knapsackRecursive(profits, weights, capacity, index + 1)
        return max(choice1, choice2)

#if __name__ == '__main__':
    '''ks = knapsack()
    profits = [1, 6, 10, 16]
    weights = [1, 2, 3, 5]

    maxProfit = ks.solveKnapsack(profits, weights, 7)
    print("Total knapsack profit --->", maxProfit)
    maxProfit = ks.solveKnapsack(profits, weights, 6)
    print("Total knapsack profit --->", maxProfit)'''


# Climbing Stairs (modified) {28/11/22}
#@lru_cache (10000)
def climbStairs(n: int) -> int:
    if n == 1 or n == 2 or n == 3:
        return n
    else:
        return climbStairs(n - 1) + climbStairs(n - 2) + climbStairs(n - 3)

def findLPSLength(s: str) -> int:
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end += 1
