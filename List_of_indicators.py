import requests
import pandas as pd # type: ignore

### URL access ###
cURL="https://api.esios.ree.es/indicators"

headers=dict()
headers['Host']="api.esios.ree.es"

### Personal token ###
headers['x-api-key']="1ec9b014c362cf015e7a17b757b3140ee29fff7481bd36b03f7d568d85fff98b"

### Request the indicator list ###
response=requests.get(cURL,headers=headers)

### Create a Data Frame ###
data=response.json()
df_indicators=pd.DataFrame(data['indicators'])

#print(df_indicators['name'],df_indicators['description'],df_indicators['short_name'],df_indicators['id'])
df_indicators=df_indicators.set_index('id')
print(df_indicators)

### Export the information to an excel ###
df_indicators.to_excel('Indicators.xlsx')
