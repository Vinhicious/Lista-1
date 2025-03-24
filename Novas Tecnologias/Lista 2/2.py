lado = int(input("Insira o temanho do quadradro: "))

print("* "*lado)
for _ in range(lado-2):
    print("* " + "  " *(lado-2)+"*")
print("* "*lado)
