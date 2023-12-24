import requests
import json

random_cockt_url= 'https://www.thecocktaildb.com/api/json/v1/1/random.php'

random_get_url=requests.get(random_cockt_url)

random_json=random_get_url.json()

# write to file
# Folder must be manually created. include file name extension
with open('Text Files/230.txt','w') as file_handler:
    # json lib, method, (content,target_file, return item indentations)
    json.dump(random_json,file_handler,indent=4)
    print('1',file_handler)
  
    


query=input('Search a cocktail: ')

search_url=f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}'

query_return=requests.get(search_url)
print('2',query_return.__str__())

query_json=query_return.json()
print('3',query_json)

if query_json['drinks']!=None:


    query_return_len=len(query_json['drinks'])
    print(f'return results: {query_return_len}')

    print('Results:\n')
    for i in range(query_return_len):
        result_names=query_json['drinks'][i]['strDrink']
        print(f'{result_names}\n')
