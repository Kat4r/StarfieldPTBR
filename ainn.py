def traduzir_palavra(palavra):
    if not any(c.isalpha() for c in palavra):
        return palavra


    pontuacao_inicio = ""
    while palavra and not palavra[0].isalpha():
        pontuacao_inicio += palavra[0]
        palavra = palavra[1:]

    pontuacao_fim = ""
    while palavra and not palavra[-1].isalpha():
        pontuacao_fim = palavra[-1] + pontuacao_fim
        palavra = palavra[:-1]

    is_maiuscula = palavra[0].isupper()

    prefixo = ""
    caule = palavra
    vogais = "aeiouy"
    for letra in palavra:
        if letra.lower() in vogais:
            break
        prefixo += letra
        caule = caule[1:]

    if not prefixo and caule != palavra:
        traducao = caule + "yay"
    else:
        traducao = caule + prefixo + "ay"


    if is_maiuscula:
        traducao = traducao.capitalize()

    traducao = pontuacao_inicio + traducao + pontuacao_fim

    return traducao


def traduzir_texto(texto):
    palavras = texto.split()
    traduzido = [traduzir_palavra(palavra) for palavra in palavras]
    return ' '.join(traduzido)

print(traduzir_texto("No persons under 14 admitted"))