import requests 
base = "https://pokeapi.co/api/v2/"
def getinfo(n):
    url = f"{base}/pokemon/{n}"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        print("data recieved")
        data = response.json()
        return data
    else:
        print("failed to retriev data {response.staus_code}")
name = "pikachu"
pokemon_data = getinfo(name)
if pokemon_data:
    print("name = ",pokemon_data["name"],"id = ",pokemon_data["id"],"height = ",pokemon_data["height"],"weight = ",pokemon_data["weight"])