frase = input("Escreva uma frase: ").lower()

print(f"Na frase \"frase}\" tem: \n",
      f"Vogal a: {frase.count("a")}",
      f"Vogal e: {frase.count("e")}",
      f"Vogal i: {frase.count("i")}",
      f"Vogal o: {frase.count("o")}",
      f"Vogal u: {frase.count("u")}")
