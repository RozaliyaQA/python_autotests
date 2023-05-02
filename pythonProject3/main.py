import requests

token = '34fb76d3650bb5a5d1a11d198738c696' # токен аккаунта

base_url = 'https://pokemonbattle.me:9104/'
'''response_add_pokemon = requests.post(f'{base_url}/pokemons', headers={'trainer_token' : token}, json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_add_pokemon.text)'''

response = requests.get(f'{base_url}pokemons',params={"trainer_id" : 4243})
print(response.text)