n = int(input("Digite a Posição da sequencia de Fibonacci: "))

if n <= 0:
    print("Posição inválida")
else:
    fibo = [1,1]
    while len(fibo)<n:
        fibo = fibo + [fibo[-1]+fibo[-2]]

print(f"Sequencia de Fibonacci {n}:", fibo)
