# **ПРИМЕРЫ**
```
from CarParkingMultiTool import LoginCarParking
import config

client=LoginCarParking(email=config.email, password=config.password)

print(f'Имя: {client.data_account.Name}\nID: {client.data_account.localID}') 
print(f'Друзья: {','.join(str(v) for v in client.data_account.FriendsID) if client.data_account.FriendsID else 'нету'}')
print(f'Деньги: {client.data_account.money}\nКоины: {client.data_account.coin}')
print(f'Анимации: {','.join(str(v) for v in client.data_account.animations) if client.data_account.animations else 'нету'}')
print(f'Флаги: {(client.data_account.flags)}')

```



