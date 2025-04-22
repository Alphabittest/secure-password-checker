import re
import string
import time

# Função para calcular o tempo estimado para quebrar a senha
def calcular_tempo_quebra(senha):
    # Caracteres possíveis para cada tipo de caractere
    simbolos = string.punctuation  # !@#$%^&*()
    maiusculas = string.ascii_uppercase  # A-Z
    minusculas = string.ascii_lowercase  # a-z
    numeros = string.digits  # 0-9

    # Número total de caracteres possíveis
    caracteres_possiveis = set()
    if bool(re.search(r'[A-Z]', senha)):  # se a senha tem maiúsculas
        caracteres_possiveis.update(maiusculas)
    if bool(re.search(r'[a-z]', senha)):  # se a senha tem minúsculas
        caracteres_possiveis.update(minusculas)
    if bool(re.search(r'\d', senha)):  # se a senha tem números
        caracteres_possiveis.update(numeros)
    if bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)):  # se a senha tem símbolos especiais
        caracteres_possiveis.update(simbolos)
    
    # Calculando o número de combinações possíveis
    num_combinacoes = len(caracteres_possiveis) ** len(senha)

    # Estimando o tempo para quebrar a senha (considerando um ataque de força bruta)
    tentativas_por_segundo = 1000000  # Estimativa de tentativas por segundo de um hacker poderoso
    tempo_segundos = num_combinacoes / tentativas_por_segundo
    tempo_formatado = format_tempo(tempo_segundos)

    return tempo_formatado


# Função para formatar o tempo estimado
def format_tempo(tempo_segundos):
    anos = int(tempo_segundos // 31536000)
    tempo_segundos %= 31536000
    dias = int(tempo_segundos // 86400)
    tempo_segundos %= 86400
    horas = int(tempo_segundos // 3600)
    tempo_segundos %= 3600
    minutos = int(tempo_segundos // 60)
    segundos = tempo_segundos % 60

    if anos > 0:
        return f"{anos} anos, {dias} dias, {horas} horas, {minutos} minutos e {segundos:.2f} segundos"
    elif dias > 0:
        return f"{dias} dias, {horas} horas, {minutos} minutos e {segundos:.2f} segundos"
    elif horas > 0:
        return f"{horas} horas, {minutos} minutos e {segundos:.2f} segundos"
    elif minutos > 0:
        return f"{minutos} minutos e {segundos:.2f} segundos"
    else:
        return f"{segundos:.2f} segundos"


# Função para verificar a força da senha
def verificar_forca(senha):
    pontuacao = 0
    criterios = {
        'Comprimento >= 8': len(senha) >= 8,
        'Letra maiúscula': bool(re.search(r'[A-Z]', senha)),
        'Letra minúscula': bool(re.search(r'[a-z]', senha)),
        'Número': bool(re.search(r'\d', senha)),
        'Símbolo': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)),
    }

    for crit, atingido in criterios.items():
        if atingido:
            pontuacao += 1
        else:
            print(f"- Falta: {crit}")

    print(f"Força da senha: {pontuacao}/5")

    # Calcular o tempo de quebra da senha
    tempo_quebra = calcular_tempo_quebra(senha)
    print(f"Tempo estimado para um hacker quebrar a senha: {tempo_quebra}")


if __name__ == "__main__":
    senha = input("Digite uma senha para verificar: ")
    verificar_forca(senha)


