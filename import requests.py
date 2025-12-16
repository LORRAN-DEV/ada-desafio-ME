import requests

def fetch_dados_paises():
    api_dos_paises = 'https://restcountries.com/v3.1/all?fields=name,population,region'
    response = requests.get(api_dos_paises)
    dados = response.json()

    return [
        {
            'Nome': pais['name']['common'],
            'População': pais['population'],
            'Região': pais['region']
        }
        for pais in dados
    ]
print(fetch_dados_paises())

senegal = requests.get('https://restcountries.com/v3.1/name/senegal').json()[0]

print("País:", senegal['name']['common'])
print("Capital:", senegal['capital'][0])
print("População:", senegal['population'])


monaco = requests.get('https://restcountries.com/v3.1/name/monaco').json()[0]
moeda=monaco['currencies']


print("País:", monaco['name']['common'])
print("Capital:", monaco['capital'][0])
print("População:", monaco['population'])
print("Moeda:", list(moeda.values())[0]['name'])


australia = requests.get('https://restcountries.com/v3.1/name/australia').json()[0]

moeda=australia['currencies']

print("País:", australia['name']['common'])
print("Capital:", australia['capital'][0])
print("População:", australia['population'])
print("Moeda:", list(moeda.values())[0]['name'])
print("Idioma:", australia['languages']['eng'])


africa=requests.get('https://restcountries.com/v3.1/region/africa').json()
print("Países da África:")  
for pais in africa:
    print("-", pais["name"]["common"])




africa = requests.get('https://restcountries.com/v3.1/independent?status=true&fields=name,region,independent').json()
for pais in africa:
    if pais["region"] == "Africa":
        print("País independente:", pais["name"]["common"])
   


  A