import json

# 1 - Strings para Dicts
pessoa = '{"nome:": "Pedro", "linguagens":["Python", "JavaScript"]}'
pessoaDict = json.loads(pessoa)
print(pessoaDict)
print(pessoaDict["linguagens"])

# 2 - Convertendo Dict para json
pessoaJson = json.dumps(pessoaDict)
print(pessoaJson)
print(type(pessoaJson))
print(type(pessoaDict))

# 3 - Formatando Json
print(json.dumps(pessoaDict, indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open("person.txt", "w") as json_file:
    json.dump(pessoaDict, json_file)
    
# 5 - Lendo json externo
with open("iris.json", "r") as f:
    data = json.load(f)
    print(data)