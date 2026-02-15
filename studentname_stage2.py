num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

result = None

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2

integer_type = ''
if(result == 0):
    integer_type = 'zero'
elif(result > 0):
    integer_type = 'positive'
else:
    integer_type = 'negative'
    
print(result,integer_type)
