# Cenário
# Sua tarefa é completar o código para avaliar a seguinte expressão:
# _____1______
# x+____1_____
#   x+___1____
#     x+__1___
#         x
# Expressão matemática
# O resultado deve ser atribuído a y. Tenha cuidado - observe os operadores e mantenha suas prioridades em mente. Não hesite em usar quantos parênteses forem necessários.
# 
# Você pode usar variáveis adicionais para encurtar a expressão (mas não é necessário). Teste seu código com cuidado.

# Dados de teste
# Exemplo de entrada: 1, 10, 100, -5

x = float(input("Digite o valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

