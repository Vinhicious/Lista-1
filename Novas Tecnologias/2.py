while True:
    num = input("Digite um número de 5 dígitos: ")

    if not num.isdigit() or len(num) != 5:
        print("Erro: Digite exatamente 5 dígitos numéricos.")
    else:
        print("   ".join(num))
        break
