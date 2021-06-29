import requests

url = "https://superheroapi.com/api/2619421814940190/search/"
super_heroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

for hero in super_heroes:
    hero_req = requests.get(url + hero['name'])
    hero['intelligence'] = hero_req.json()['results'][0]['powerstats']['intelligence']
super_intel = (sorted(super_heroes, key=lambda hero: hero['intelligence'])[0]['name'])
print(f'Cамый умный супер герой  - {super_intel} ')
