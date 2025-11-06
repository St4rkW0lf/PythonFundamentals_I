# Cenário:
# Um número natural é considerado primo se for maior que 1 e não tiver divisores
# diferentes de 1 e dele próprio.
# Exemplo: 8 não é primo (divisível por 2 e 4), enquanto 7 é primo.
#
# Tarefa:
# Criar uma função chamada is_prime que receba um número e retorne True se ele for
# primo, ou False caso contrário.
#
# Dica:
# Tente dividir o número por todos os valores de 2 até a raiz quadrada do número.
# Se algum divisor deixar resto zero, o número não é primo.
# A raiz quadrada pode ser obtida com o operador ** (x ** 0.5).

def is_prime(num):
    # Números menores ou iguais a 1 não são primos
    if num <= 1:
        return False

    # Testa divisores de 2 até a raiz quadrada do número
    for i in range(2, int(num ** 0.5) + 1):
        # Se o número for divisível por i, não é primo
        if num % i == 0:
            return False

    # Se nenhum divisor foi encontrado, o número é primo
    return True


# Teste da função: exibe números primos de 2 a 20
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
