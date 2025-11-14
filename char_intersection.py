# Lê as frases
frase1 = input()
frase2 = input()

# Cria sets das palavras
set1 = set(frase1.split())
set2 = set(frase2.split())

# Interseção dos sets
comum = set1 & set2

# Adiciona '?' às palavras comuns
resultado = {palavra + "?" for palavra in comum}

# Ordena alfabeticamente e imprime
print(" ".join(sorted(resultado)))