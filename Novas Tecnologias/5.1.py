while True:
    numero = input("Digite um número de 4 dígitos: ")

    if len(numero) == 4 and numero.isdigit():
        primeiro = (int(numero[0]) + 7) % 10
        segundo = (int(numero[1]) + 7) % 10
        terceiro = (int(numero[2]) + 7) % 10
        quarto = (int(numero[3]) + 7) % 10

        temp = primeiro
        primeiro = quarto
        quarto = temp
        temp = segundo
        segundo = terceiro
        terceiro = temp

        print(f"Dígitos criptografados: {primeiro}{segundo}{terceiro}{quarto}")
        break
    else:
        print("Erro: Digite um número válido de 4 dígitos.")
