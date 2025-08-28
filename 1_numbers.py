#taking function that contains a number and a format specifier
def format_function(num , oct):
    result = format(num , oct)
    return result
#calling the function and storing result 
Formatted_value = format_function(145 , 'o') # 'o' is the format specifier for octal representation
print(Formatted_value)