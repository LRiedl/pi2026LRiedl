# viewtreinos.py

def mostrar_registros(registros):
    for registro in registros:
        nome, idade, sexo, exercicio, grupo, carga, series, repeticoes, treino = registro.strip().split(",")
        print("-" * 30)
        print("Nome:", nome)
        print("Idade:", idade)
        print("Sexo:", sexo)
        print("Exercício:", exercicio)
        print("Grupo muscular:", grupo)
        print("Carga:", carga)
        print("Séries:", series)
        print("Repetições:", repeticoes)
        print("Treino:", treino)

def mostrar_uma_linha(titulo, valor):
    print("-" * 30)
    print(titulo)
    print(valor)
