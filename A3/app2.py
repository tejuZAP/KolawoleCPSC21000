'''
3Algorithm for a program that will ask the user to enter numbers and then will report the mean of those numbers"
'''

def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
#Gets the numbers from the user
numbers = []
while True:
    try:
        user_input = input("Enter some numbers:")
        if user_input.lower() == 'done':
            break
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid")
#Calculate and display mean
mean = calculate_mean(numbers)
print(mean)