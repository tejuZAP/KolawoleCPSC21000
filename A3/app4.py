'''
Calculates the spread of a range of numbers
'''

list1 = [8, 6, 2, 4, 65, 71, 5] 

#calculates the difference between the max and min
def calculate_spread(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)
#prints spread
spread = calculate_spread(list1)
print(spread)