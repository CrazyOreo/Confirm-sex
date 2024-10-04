valor=input("Por favor, insira seu sexo\n")

if valor == "F" :
    print("Feminino")
elif valor=="M":
    print("Masculino")
else :
    while valor not in ["F", "M","f","m"]:
        print ("Sexo incorreto!\n")
        valor=input("Por favor, insira o seu sexo\n")
        if valor == "F" or "f" :
            print("Feminino")
        elif valor=="M" or "m":
            print("Masculino")