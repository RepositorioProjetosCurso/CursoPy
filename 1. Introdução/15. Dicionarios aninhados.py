import pprint
gamesDict = {
    'Residente Evil 4': {
        'yearLaunch': 2024,
        'classification': 9.3,
        'genre': ['Ação', 'Aventura']
    },
    'Mario Odyssey': {
        'yearLaunch': 2022,
        'classification': 8.6,
        'genre': ['3D', 'Aventura']
    },
    'Donkey Kong': {
        'yearLaunch': 1995,
        'classification': 10,
        'genre': ['Aventura', 'Plataforma']
    }
}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(gamesDict)

# 1 - Buscar informação de um dict aninhado
print(gamesDict['Mario Odyssey']['genre'])

# 2 - Adicionar um item ao dict
gamesDict['Mario Odyssey']['players'] = 1
print(gamesDict['Mario Odyssey'])

# 3 - Excluir um dicionario
del gamesDict['Mario Odyssey']
pp.pprint(gamesDict)