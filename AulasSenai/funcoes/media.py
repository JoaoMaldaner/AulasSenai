def ler_notas():
    notas = []

    quantidade = int(input("Quantas notas deseja informar? "))

    for i in range(quantidade):
        nota = int(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)

    return notas


def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return float(media)

def ler_media():
    notas = ler_notas()
    media = calcular_media(notas)

    print("\nNotas informadas: ", notas)
    print(f"Média = {media:.2f}")

ler_media()

