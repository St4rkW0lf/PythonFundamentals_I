# Cenário
# Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números: 1, 2, 3, 4 e 5.
# 
# Sua tarefa:
# 
# escreva uma linha de código que solicite que o usuário substitua o número do meio na lista por um número inteiro inserido pelo usuário (Etapa 1)
# escreva uma linha de código que remova o último elemento da lista (Etapa 2)
# escreva uma linha de código que imprima o comprimento da lista atual (Etapa 3).
# Pronto para este desafio?


hat_list = [1, 2, 3, 4, 5]  # Esta é a lista atual de números ocultos no chapéu.

# Etapa 1: substituir o número do meio por um número inserido pelo usuário
hat_list[2] = int(input("Digite um número inteiro para substituir o número do meio: "))

# Etapa 2: remover o último elemento da lista
hat_list.pop()

# Etapa 3: imprimir o comprimento da lista atual
print("O comprimento da lista atual é:", len(hat_list))

# Exibir a lista final
print(hat_list)
