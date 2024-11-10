CONTACT [TELEGRAM](t.me/CarParkingMultiTool)

![PyPI - Version](https://img.shields.io/pypi/v/requests)

___
# DESCRIPTION
**RU: Данный модуль подключаться к серверам Car Parking и с помощью этого их можно "взламывать"**


**ENG: This module connects to Car Parking servers and can be used to "hack" them**


___

# **EXAMPLES**

1№

*CODE*:
```python
from CarParkingMultiTool import LoginCarParking
import config


client=LoginCarParking(email=config.email, password=config.password)

#Ввывод ID и имя / Input ID and name
print(f'Name: {client.data_account.Name}\nID: {client.data_account.localID}')

#Ввывод друзей / Input friends
print(f'Friends: {','.join(str(v) for v in client.data_account.FriendsID) if client.data_account.FriendsID else 'no'}')

#Ввывод валюта / Input ID and currency
print(f'Money: {client.data_account.money}\nCoin: {client.data_account.coin}')

#Ввывод анимаций и флаг / Input animations and flags
print(f'Animation: {','.join(str(v) for v in client.data_account.animations) if client.data_account.animations else 'no'}')
print(f'Flag: {(client.data_account.flags)}')

```
RESULT
```
Name: Player#471
ID: MC551684
Friends: no
Money: 68000
Coin: 0
Animation: no
Flag: {}
```
___
2№

*CODE*:
```python
from CarParkingMultiTool import LoginCarParking
import config


client=LoginCarParking(email=config.email, password=config.password)
#Ввывод валюта / Input ID and currency
print('it was')
print(f'Money: {client.data_account.money}\nCoin: {client.data_account.coin}')
print('-----------------------------------------------------')
print('Cheat money')
money=int(input('How many>>'))
#Накрутка денег / Cheating money
client.hack_money(money) # Заменяет(не добавляет) / Replaces (does not add)
client.update() #обновляем информацию с кэкзампляре / updating information from the k instances
print('has become')
print(f'Money: {client.data_account.money}\nCoin: {client.data_account.coin}')

```
RESULT
```
it was
Money: 68000
Coin: 0
#-----------------------------------------------------#
Cheat money
How many>>10000000 
has become
Money: 10000000
Coin: 0
```





