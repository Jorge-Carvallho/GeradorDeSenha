🔑 Gerador de Senhas em Python

Este é um projetinho de estudo em Python para gerar senhas aleatórias de acordo com as preferências do usuário.
Ele utiliza a biblioteca padrão random e string.


🚀 Como funciona

O programa permite que você escolha:

O tamanho da senha

Se deseja incluir:

Letras maiúsculas (A–Z)

Letras minúsculas (a–z)

Dígitos (0–9)

Símbolos (caracteres especiais, como !@#$%)

Caso nenhum tipo de caractere seja selecionado, o programa gera um erro explicando que pelo menos um tipo precisa ser escolhido.


▶️ Como rodar o projeto

Clone ou baixe este repositório.

Entre na pasta do projeto pelo terminal:

cd nome-da-pasta

Execute o programa com Python3:

python3 nome_do_arquivo.py


Exemplo:

cd gerador-senha
python3 gerador.py

📋 Exemplo de uso
############# Gerador de Senha ##############
Digite o tamanho da senha: 12
Deseja usar letra maiusculas? (s/n): s
Deseja usar senha minusculas? (s/n): s
Deseja usar digitos?  (s/n): s
Deseja usar simbolos? (s/n): n

Senha Gerada ------------> Xq3fWkG72bLm


🛠️ Tecnologias utilizadas

Python 3

Módulos: random e string (ambos da biblioteca padrão do Python)


📂 Estrutura do código

gerar_senha(...): Função principal que monta a senha conforme as opções escolhidas.

Entrada do usuário para decidir os parâmetros.

Impressão da senha gerada.


📌 Aprendizados neste projeto

Uso do módulo random para escolher caracteres aleatórios.

Uso do módulo string para acessar grupos de caracteres (ascii_uppercase, ascii_lowercase, digits, punctuation).

Estrutura condicional para montar o conjunto de caracteres.

Uso de raise para tratamento de erro.