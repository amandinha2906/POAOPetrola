def ler_vogais():
    letras = []
    for i in range(7):
        letra = input(f"Digite o {i+1}º letra: ")
        letras.append(letra)
    return letras

def mostrar_vogais(letras):
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogais_enc = [letra for letra in letras if letra.lower() in vogais]
    print("As vogais encontradas são: ")
    for vogal in vogais_enc:
        print(vogal, end=" ")

def main():
    vetor = ler_vogais()
    mostrar_vogais(vetor)

if __name__ == "__main__":
    main()
