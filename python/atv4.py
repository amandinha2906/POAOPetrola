
def calcular_media(notas):
    return sum(notas) / len(notas)


medias_maior_que_7 = []


for aluno in range(1, 11):
    print(f"Notas do aluno {aluno}:")
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Informe a nota {i}: "))
        notas.append(nota)
    

    media = calcular_media(notas)
    
    if media > 7:
        medias_maior_que_7.append(media)


print("\nMédias maiores que 7:")
for media in medias_maior_que_7:
    print(media)
