# Cenário
# Sua tarefa aqui é ainda mais especial do que antes: você deve reprojetar o (feio) comedor de vogal do laboratório anterior e criar um melhor (bonito) comedor de vogal! Escreva um programa que use:
# 
# um loop for
# o conceito de execução condicional (if-elif-else)
# a declaração continue.
# Seu programa deve:
# 
# peça ao usuário para inserir uma palavra;
# use user_word = user_word.upper() para converter em maiúsculas a palavra inserida pelo usuário; falaremos sobre métodos de string e o método upper() muito em breve - não se preocupe;
# use execução condicional e a declaração continue para "consumir" as seguintes vogais A, E, I, O, U da palavra inserida;
# atribua as letras não consumidas à variável word_without_vowels e imprima a variável na tela.
# Veja o código no editor. Criamos word_without_vowels e atribuímos uma string vazia a ela. Use a operação de concatenação para pedir ao Python que combine letras selecionadas em uma sequência mais longa durante as voltas de loop subsequentes e atribua-a à variável word_without_vowels.
# 
# Teste seu programa com os dados que fornecemos para você.


word_without_vowels = ""

# Solicita que o usuário digite uma palavra
user_word = input("Digite uma palavra: ")

# Converte a palavra para maiúsculas
user_word = user_word.upper()

# Loop para percorrer cada letra
for letter in user_word:
    # Se for vogal, pula para a próxima iteração
    if letter in "AEIOU":
        continue
    # Caso contrário, adiciona a letra à nova palavra
    word_without_vowels += letter

# Imprime a palavra sem vogais
print(word_without_vowels)
