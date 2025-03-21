import math

x1 = float(input("Digite a coordenada x1 do primeiro ponto: "))
y1 = float(input("Digite a coordenada y1 do primeiro ponto: "))
x2 = float(input("Digite a coordenada x2 do segundo ponto: "))
y2 = float(input("Digite a coordenada y2 do segundo ponto: "))
            
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"A distância entre os pontos é: {distancia:.2f}")

