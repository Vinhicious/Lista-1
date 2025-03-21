frase = input("Escreva uma frase: ").upper()
contagem = 0

for letra in frase:
    if letra in 'AEIOU':
        contagem += 1

print(f" A frase possui {contagem} vogais")
