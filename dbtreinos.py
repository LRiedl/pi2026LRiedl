# Model
ARQUIVO = "treinos.csv"

def todos():
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return arquivo.readlines()

def contar_exercicios():
    registros = todos()
    return len(registros)

def por_exercicio(nome_exercicio):
    registros = todos()
    encontrados = []

    for registro in registros:
        nome, idade, sexo, exercicio, grupo, carga, series, repeticoes, treino = registro.strip().split(",")
        if exercicio.lower() == nome_exercicio.lower():
            encontrados.append(registro)

    return encontrados

def por_grupo(nome_grupo):
    registros = todos()
    encontrados = []

    for registro in registros:
        nome, idade, sexo, exercicio, grupo, carga, series, repeticoes, treino = registro.strip().split(",")
        if grupo.lower() == nome_grupo.lower():
            encontrados.append(registro)

    return encontrados

def maior_carga():
    registros = todos()

    maior = 0
    nome_maior = ""
    exercicio_maior = ""

    for registro in registros:
        nome, idade, sexo, exercicio, grupo, carga, series, repeticoes, treino = registro.strip().split(",")
        if int(carga) > maior:
            maior = int(carga)
            nome_maior = nome
            exercicio_maior = exercicio

    return nome_maior, exercicio_maior, maior

def carga_media():
    registros = todos()

    soma = 0

    for registro in registros:
        nome, idade, sexo, exercicio, grupo, carga, series, repeticoes, treino = registro.strip().split(",")
        soma += int(carga)

    if len(registros) == 0:
        return 0

    return soma / len(registros)

def volume_total():
    registros = todos()

    volume = 0

    for registro in registros:
        nome, idade, sexo, exercicio, grupo, carga, series, repeticoes, treino = registro.strip().split(",")
        volume += int(carga) * int(series) * int(repeticoes)

    return volume

def grupo_mais_treinado():
    registros = todos()
    grupos = {}

    for registro in registros:
        nome, idade, sexo, exercicio, grupo, carga, series, repeticoes, treino = registro.strip().split(",")
        if grupo in grupos:
            grupos[grupo] += 1
        else:
            grupos[grupo] = 1

    maior_grupo = ""
    maior_quantidade = 0

    for grupo in grupos:
        if grupos[grupo] > maior_quantidade:
            maior_quantidade = grupos[grupo]
            maior_grupo = grupo

    return maior_grupo, maior_quantidade

def treino_mais_volume():
    registros = todos()
    treinos = {}

    for registro in registros:
        nome, idade, sexo, exercicio, grupo, carga, series, repeticoes, treino = registro.strip().split(",")
        valor = int(carga) * int(series) * int(repeticoes)

        if treino in treinos:
            treinos[treino] += valor
        else:
            treinos[treino] = valor

    maior_treino = ""
    maior_volume = 0

    for treino in treinos:
        if treinos[treino] > maior_volume:
            maior_volume = treinos[treino]
            maior_treino = treino

    return maior_treino, maior_volume

def evolucao_exercicio(nome_exercicio):
    registros = por_exercicio(nome_exercicio)

    if len(registros) == 0:
        return None

    primeiro = registros[0].strip().split(",")
    ultimo = registros[-1].strip().split(",")

    carga_inicial = int(primeiro[5])
    carga_final = int(ultimo[5])

    return carga_inicial, carga_final, carga_final - carga_inicial
