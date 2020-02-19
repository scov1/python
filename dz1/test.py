
from collections import namedtuple
import random

_alphabet = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

User = namedtuple('User',('fullName','id','position','login','password'))
users=[]


with open('users.txt') as file:
    for i in file:
        line = i.split(':')
        fullName = f'{line[1][0]}.{line[2][0]}.{line[3]}'
        position = line[4]
        login=''.join(random.choice(_alphabet) for i in range(5))
        password=''.join(random.choice(_alphabet) for i in range(5))
        _str = User(fullName,line[0],position,login,password)
        users.append(_str)

print(f'\n\nFull name\t\tid\t\tPosition\t\tLogin\t\t\t\tPassword\n')

for u in users:
    print(f'{u.fullName}\t\t{u.id}\t\t{u.position}\t\t\t\t\t\t\t\t{u.login}\t\t\t\t{u.password}')
