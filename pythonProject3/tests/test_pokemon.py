import requests
import pytest

def test_status_code():
    token = '34fb76d3650bb5a5d1a11d198738c696'
    response = requests.post('https://pokemonbattle.me:9104/pokemons', headers={'trainer_token': token}, json = {
    "name": "Pyt",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}) 
    assert response.status_code == 400


def test_part_of_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params = {'trainer_id' : 4243})
    assert response.json()['trainer_name'] == 'Розалия'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Розалия'), ('city', 'Спб')])

def test_parts_of_body(key, value):
    response = requests.get('https://pokemonbattle.me:9104/trainers', params = {'trainer_id' : 4243})
    assert response.json()[key] == value
