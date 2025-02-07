import random

def obter_palpite():
    return int(input("Digite seu palpite: "))

def verificar_palpite(palpite, numero_secreto):
    if palpite == numero_secreto:
        return "correto"
    elif (palpite > numero_secreto and palpite - numero_secreto <= 10) or (palpite < numero_secreto and numero_secreto - palpite <= 10):
        return "quente"
    else:
        return "frio"

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    palpite = -1  

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while palpite != numero_secreto:
        tentativas += 1
        palpite = obter_palpite()
        resultado = verificar_palpite(palpite, numero_secreto)

        if resultado == "correto":
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        elif resultado == "quente":
            print("Está quente! Você está perto.")
        else:
            print("Está frio! Tente novamente.")

def main():
    jogar_adivinhacao()

if __name__ == "__main__":
    main()
