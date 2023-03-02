base_url = "https://pokeapi.co/api/v2"
api_method = "pokemon/squirtle"
name = "Name"

api_url = f"{base_url}{api_method}?&q={name}"

print(api_url)


res = requests .__get(f"https://pokeapi.co/api/v2/pokemon/{squirtle}")

     
    def _get(self, q=''):
        res = requests.get(f'{self.base_url}/current.json?key={self.api_key}&q={q}')
        if res.ok:
            return res.json()
pokemon1 =("Get info on pokemon")
data = poke_res.json()

print(data.get("abilities"))