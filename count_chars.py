#guarda o input que o utilizador dá
frase = input()

#cria um dicionário vazio
dicionario = {}

#ciclo for para percorrer cada carácter da frase,,um de cada vez
#verifica se a letra ainda não foi adicionada ao dicionário
#conta quantas vezes a letra aparece e guarda no dicionário
for letra in frase:
    if letra not in dicionario:
        dicionario[letra] = frase.count(letra)


#mostra o dicionário obtido
print(dicionario)

