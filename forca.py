import random

print("JOGO DA FORCA")

palavras= ["casa", "macaco", "boneca", "melancia", "gato"]
secreta = random.choice(palavras)
tamanho= len(secreta)
print(tamanho)
espacos = ["_"]*tamanho
print(espacos)

while "_" in espacos:
    usuario= input("digite uma letra:").lower()
    if usuario in secreta:
        print("correto")
        for i,letra in enumerate(secreta):
            if usuario == letra:
                print(f"existe a letra {usuario} na posição {i+1}")
                espacos[i]=usuario
    else:
       print("errado")


    print(espacos)

print("vc ganhooou!!!!")