import re

result = re.search(r'Analytics', 'AV Analytics Vidhya  Analytics AV')
print(result.start())
print(result.end())


res_1 = re.search(r'[0-6]', 'Number: 5').group()
print(res_1)

#\w матчит любую букву цифру или знак подчеркивания
print("Lowercase w:", re.search(r'Co\w\wk\we', 'Co1okie').group())
print("Lowercase w:", re.search(r'Co\w\wk\we', 'Coaokie').group())

#findall все соответствия выводим в виде списка
result_findall = re.findall(r'Analyti\ws', 'AV Analytics Vidhya  Analytics AV')
print(result_findall)