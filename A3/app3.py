'''
fibonacci sequence - [0, 1, 1, 2, 3, 5, 8, 13, ...]
'''

def fibonnaci(n):
    nums = [0, 1]
    for i in range(n):
        print(i)
        if i > 1:
            nums.append(nums[i-2] + nums[i-1])
            
    return nums[-1]

print(fibonnaci(8))