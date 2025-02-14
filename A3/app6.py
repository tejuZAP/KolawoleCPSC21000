'''
converts hexadecimal to base 10 value
'''
def hex_to_decimal(hex_number):
    return int(hex_number, 16)

hex_value = "" #enter a hexadecimal
decimal_value = hex_to_decimal(hex_value)
print(decimal_value)