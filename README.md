# **ПРИМЕРЫ**
```
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



