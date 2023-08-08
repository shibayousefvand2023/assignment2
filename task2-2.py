from aifc import Error
import operator
from unittest import result


a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))
if operator == a < b + c:
    result = 'OK'
else:
    result = 'Error'
print(result)
if operator == b < a + c:
    result = 'OK'
else:
    result = 'Error'
print(result)
if operator == c < a + b:
    result = 'OK'
else:
    result = 'Error'
print(result)
