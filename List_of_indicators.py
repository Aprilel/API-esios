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

### Export the information to an excel ###
df_indicators.to_excel('Indicators.xlsx')

### Add the necessary parameters for indicator search ##
indicator=input("introduce el id del indicador que quieres consultar y pulsa ENTER: ")
start_date=input("introduce la fecha inicial en formato YYYY-MM-DDT00:00:00Z y pulsa ENTER: ")
end_date=input("introduce la fecha final en formato YYYY-MM-DDT00:00:00Z y pulsa ENTER: ")

### Form the complete URL ###
cURLwithIndicator=cURL+"/"+indicator+"?start_date="+start_date+"&end_date="+end_date

### Obtain the response and export to Excel ###
response=requests.get(cURLwithIndicator,headers=headers)
data=response.json()
df_values=pd.DataFrame(data['indicator']['values'])
df_values.to_excel('Values_'+indicator+'.xlsx')