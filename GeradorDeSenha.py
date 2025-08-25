import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True, usar_simbolos=True):
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase

    if usar_minusculas:
        caracteres += string.ascii_lowercase

    if usar_digitos:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError('Pelo menos 1 tipo de caracteres deve ser selecionado.')
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("############# Gerador de Senha ##############")

tamanho = int(input('Digite o tamanho da senha: '))
usar_maiusculas = input('Deseja usar letra maiusculas? (s/n): ').lower() == 's'
usar_minusculas = input('Deseja usar senha minusculas? (s/n): ').lower() == 's'
usar_digitos = input('Deseja usar digitos?  (s/n): ').lower() == 's'
usar_simbolos = input('Deseja usar simbolos? (s/n): ').lower() == 's'

senha_gerada = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_digitos, usar_simbolos)
print(f'Senha gerada ----> {senha_gerada}')

