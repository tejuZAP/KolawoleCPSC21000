y = input("provide numbers to multiply")
parts = y.split("")
numbers = []
for parts in parts:
    numbers.append(int(part))
    
    total=1
    for num in numbers:
        total= total * num
 
     print(total)   