# ordenando as indices dentro de uma lista


linguagens = ['python', 'csharp', 'java', 'c']
linguagens.sort(key=lambda x: len(x))

print(linguagens)