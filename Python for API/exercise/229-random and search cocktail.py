import requests

query=input('Search a cocktail: ')

search_url=f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}'

query_return=requests.get(search_url)
if query_return.__str__()=='<Response [200]>':
    query_json=query_return.json()
    print(query_json)

    query_return_len=len(query_json['drinks'])
    print(f'return results: {query_return_len}')
# query -> search -> return -> json

random_url='https://www.thecocktaildb.com/api/json/v1/1/random.php'

random_return=requests.get(random_url)
random_json=random_return.json()

print(random_json)

random_name=random_json['drinks'][0]['strDrink']
print(f'Name: {random_name}')
