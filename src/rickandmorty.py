import requests
import json

class Rickandmorty:
    
    def get_images(self) -> str:
        URL = 'https://rickandmortyapi.com/api/character/'
        response = requests.get(URL)
        images = []

        if response.status_code == 200:
            diccionario = json.loads(response.text)
            for datos in diccionario['results']:
                images.append(datos['image'])
        else:
            print('Se ha generado un error!')
        return images
