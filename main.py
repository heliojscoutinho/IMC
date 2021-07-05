nome = str(input("Digite o seu nome: "))
sexo = str(input("Digite o seu sexo (H - Homem / M - Mulher): "))
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)

if sexo == "H":
    if imc < 20.7:
        print(f"Olá {nome}.Seu IMC é: {imc:.2f}. Abaixo do peso!")
    elif 20.7 <= imc <= 26.4:
        print(f"Olá {nome}. Seu IMC é: {imc:.2f}. Peso ideal!")
    elif 26.5 <= imc <= 27.8:
        print(f"Olá {nome}. Seu IMC é: {imc:.2f}. Pouco acima do peso!")
    elif 27.9 <= imc <= 31.1:
        print(f"Olá {nome}. Seu IMC é: {imc:.2f}. Acima do peso!")
    elif imc >= 31.2:
        print(f"Olá {nome}. Seu IMC é: {imc:.2f}. Obesidade!")
if sexo == "M":
    if imc < 19.1:
        print(f"Olá {nome}. Seu IMC é: {imc:.2f}. Abaixo do peso!")
    elif 19.0 <= imc <= 25.8:
        print(f"Olá {nome}. Seu IMC é: {imc:.2f}. Peso ideal!")
    elif 25.9 <= imc <= 27.3:
        print(f"Olá {nome}. Seu IMC é: {imc:.2f}. Pouco acima do peso!")
    elif 27.4 <= imc <= 32.3:
        print(f"Olá {nome}. Seu IMC é: {imc:.2f}. Acima do peso!")
    elif imc >= 32.4:
        print(f"Olá {nome}. Seu IMC é: {imc:.2f}. Obesidade!")
