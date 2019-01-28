'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

given, k, i = [10, 5, 3, 7], 17, 0
while i < len(given):
    stack = given[i]
    for num in given:
        if num == stack:
            pass
        else:
            if stack + num == k:
                print(stack, '+', num, ' = ' , k , ', true')
            else:
                print(stack, '+', num, ' = ' , k , ', false')
    i+=1
    
