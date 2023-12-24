import requests
cocktail_id='11007'

# when creating a url, include: 'https://' in the beginning
url=f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={cocktail_id}'

access_site=requests.get(url)

# json-ify the http request
json_data=access_site.json()

# __str__() method of the object
print(access_site)

# json() method of the object
print(json_data,'\n')

# all the properties of the 1st result of query {it's a dict}
print(json_data['drinks'][0])
