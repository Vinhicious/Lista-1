n = int(input("Digite um número: "))

primos = [True]*(n+1)

primos[0:2] = [False, False]
        
for i in range(2, int((n**0.5))+1):
    if primos[i]:
        for j in range(i*i, n+1, i):
            primos[j]=False
            
print(primos)

print([i for i, primo in enumerate(primos) if primo])
