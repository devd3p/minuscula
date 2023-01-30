def tem_minusculas(palavra):
    palavra = input('Digite uma palavra:')
    for letra in palavra:
        if letra == letra.lower():
            return f'{palavra} tem minúscula.'
    return f'{palavra} não tem minúscula.'