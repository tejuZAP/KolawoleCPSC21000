list1 = [0, 1, 2, 4, 65, 71, 2] # 71
list2 = [2, 9, 5, 2, 1, 5] # 9

def findMaximum(listOfNumbers):
    max = listOfNumbers[0]
    for item in listOfNumbers:
        print(item, max)
        if item > max:
            max = item
    return max

print(findMaximum(list1))
print(findMaximum(list2))