# Cenário
# Ouça esta história: um garoto e seu pai, um programador de computador, estão jogando com blocos de madeira. Eles estão construindo uma pirâmide.
# 
# A pirâmide deles é um pouco esquisita, pois na verdade é uma parede em forma de pirâmide - é plana. A pirâmide é empilhada de acordo com um princípio simples: cada camada inferior contém um bloco a mais do que a camada acima.
# Sua tarefa é escrever um programa que lê o número de blocos que os construtores têm e gera a altura da pirâmide que pode ser construída usando esses blocos.
# 
# Nota: a altura é medida pelo número de camadas totalmente concluídas; se os construtores não tiverem um número suficiente de blocos e não puderem concluir a próxima camada, eles terminarão seu trabalho imediatamente.
# 
# Teste seu código usando os dados que fornecemos.

blocks = int(input("Insira o número de blocos: "))

altura = 0
camada = 1  # número de blocos necessários para a próxima camada

# Enquanto ainda houver blocos suficientes para formar uma nova camada
while blocks >= camada:
    blocks -= camada      # usa blocos para formar a camada atual
    altura += 1           # aumenta a altura da pirâmide
    camada += 1           # a próxima camada precisará de mais 1 bloco

print("A altura da pirâmide:", altura)
