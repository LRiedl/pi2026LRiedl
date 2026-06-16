# listar_treinos.py

import dbtreinos
import viewtreinos

def menu():
    print("\nPI 2026 - Controle de Treinos e Evolução")
    print("1 - Listar todos os registros")
    print("2 - Listar exercícios por grupo")
    print("3 - Listar exercícios por nome")
    print("4 - Mostrar maior carga")
    print("5 - Mostrar carga média")
    print("6 - Mostrar volume total")
    print("7 - Mostrar grupo mais treinado")
    print("8 - Mostrar treino com maior volume")
    print("9 - Mostrar evolução de um exercício")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registros = dbtreinos.todos()
        viewtreinos.mostrar_registros(registros)

    elif opcao == "2":
        grupo = input("Digite o grupo muscular: ")
        registros = dbtreinos.por_grupo(grupo)
        viewtreinos.mostrar_registros(registros)

    elif opcao == "3":
        exercicio = input("Digite o exercício: ")
        registros = dbtreinos.por_exercicio(exercicio)
        viewtreinos.mostrar_registros(registros)

    elif opcao == "4":
        nome, exercicio, carga = dbtreinos.maior_carga()
        viewtreinos.mostrar_uma_linha("Maior carga registrada:", f"{nome} - {exercicio} - {carga} kg")

    elif opcao == "5":
        media = dbtreinos.carga_media()
        viewtreinos.mostrar_uma_linha("Carga média:", f"{media:.2f} kg")

    elif opcao == "6":
        volume = dbtreinos.volume_total()
        viewtreinos.mostrar_uma_linha("Volume total de treino:", f"{volume} kg")

    elif opcao == "7":
        grupo, quantidade = dbtreinos.grupo_mais_treinado()
        viewtreinos.mostrar_uma_linha("Grupo mais treinado:", f"{grupo} ({quantidade} registros)")

    elif opcao == "8":
        treino, volume = dbtreinos.treino_mais_volume()
        viewtreinos.mostrar_uma_linha("Treino com maior volume:", f"{treino} ({volume} kg)")

    elif opcao == "9":
        exercicio = input("Digite o exercício: ")
        resultado = dbtreinos.evolucao_exercicio(exercicio)

        if resultado is None:
            print("Exercício não encontrado.")
        else:
            carga_inicial, carga_final, evolucao = resultado
            print("-" * 30)
            print("Exercício:", exercicio)
            print("Carga inicial:", carga_inicial, "kg")
            print("Carga final:", carga_final, "kg")
            print("Evolução:", evolucao, "kg")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
