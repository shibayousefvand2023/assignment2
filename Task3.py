from aifc import Error
from locale import YESEXPR
import operator
from unittest import result


a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))
if operator == a < b + c:
    result = 'YESEXPR'
else:
    result = 'Error'
print(result)
if operator == b < a + c:
    result = 'YESEXPR'
else:
    result = 'Error'
print(result)
if operator == c < a + b:
    result = 'YESEXPR'
else:
    result = 'Error'
print(result)

