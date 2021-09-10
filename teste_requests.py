import requests
import jsonpath

# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

#print(dir(avaliacoes)
resut = jsonpath.jsonpath(avaliacoes.json(), 'results')

print(resut)




#GET Cursos

headers = {'Authorization':'Token ead7c481c09b9408e191559f375e8432b2525789'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

#print(cursos.status_code)
#print(cursos.json())