"""
Question:
Write a function `solution(A)` that takes an array `A` of `N` integers as input and returns the smallest positive integer (greater than 0) that does not occur in the array.

Example:
Given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [-1, -3], the function should return 1.

Assume:
- N is an integer within the range [1..100,000].
- Each element of array A is an integer within the range [-1,000,000..1,000,000].

Write an efficient algorithm for the above problem.
"""


def solution(A):
    A = set(A)  # Convert list to set for O(1) lookups
    smallest = 1
    while smallest in A:
        smallest += 1
    return smallest


### Explanation
- Convert the list to a set for faster lookup.
- Start from `1` and increment until a number is not found in the set.
- Time complexity: **O(N)**
- Space complexity: **O(N)**