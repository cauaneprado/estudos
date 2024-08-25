print("CONVERSOR DE MOEDAS")

while True:
    print("ESCOLHA UMA DAS OPÇÕES DISPONÍVEIS:")
    print("[1] DÓLAR")
    print("[2] EURO")
    print("[3] LIBRA")
    print("[4] FRANCO SUÍÇO")
    print("[5] ENCERRAR")

    opcao = int(input("Selecione uma opção: "))
    if opcao == 5:
        break
    real = float(input("Qual o valor do dinheiro que você tem? R$ "))

    dolar = real / 5.54
    euro = real / 6.21
    libra = real / 7.33
    franco = real / 6.54

    if opcao == 1:
        print(f"Você tem ${dolar:.2f} em Dólar.")
    elif opcao == 2:
        print(f"Você tem €{euro:.2f} em Euro.")
    elif opcao == 3:
        print(f"Você tem £{libra:.2f} em Libra.")
    elif opcao == 4:
        print(f"Você tem CHF{franco:.2f} em Franco Suíço.")


    