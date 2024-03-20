def ler_vetor():
    vetor = []
    for i in range(15):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        vetor.append(numero)
    return vetor

def mostrar_vetor(vetor):
    print("Vetor lido:")
    for numero in vetor:
        print(numero, end=" ")

def main():
    vetor = ler_vetor()
    mostrar_vetor(vetor)

if __name__ == "__main__":
    main()
