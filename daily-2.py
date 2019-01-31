'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

given = input().split()
given = list(map(int, given))
result = []

for num1 in given:
    x = 1
    for num2 in given:
        if num1!=num2:
           x *= num2
    result.append(x)
print(result)
