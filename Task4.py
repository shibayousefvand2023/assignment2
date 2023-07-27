from locale import normalize
from token import GREATER


name = input('Enter name:')
familly = input('Enter familly:')
lesson1 = float(input('biology:'))
lesson2 = float(input('english:'))
lesson3 = float(input('chemestry:'))
Average = float((lesson1+lesson2+lesson3)/3)
if Average == >17:
    status = 'GREATER'
if Average == "12<=Average>17":
    status = 'normalize'
if Average== <12:
    status = 'failed'
print('name :' ,'familly :' , Average , 'Average :' , status)



