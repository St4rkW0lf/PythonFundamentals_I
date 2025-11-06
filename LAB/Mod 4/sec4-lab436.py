# Cenário
# Sua tarefa é escrever e testar uma função que usa três argumentos (um ano, um mês e um dia do mês) 
# e retorna o dia correspondente do ano ou retorna None se algum dos argumentos for inválido.
#
# Use as funções escritas e testadas anteriormente. 
# Adicione seus próprios casos de teste ao código.


# Código
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29
    else:
        return month_days[month - 1]


def day_of_year(year, month, day):
    # Verifica validade do mês e do dia
    if month < 1 or month > 12:
        return None

    days = days_in_month(year, month)
    if days is None or day < 1 or day > days:
        return None

    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)

    total_days += day
    return total_days


# Casos de teste
print(day_of_year(2000, 12, 31))  # 366 (ano bissexto)
print(day_of_year(2019, 12, 31))  # 365 (ano comum)
print(day_of_year(2020, 2, 29))   # 60  (ano bissexto)
print(day_of_year(2021, 2, 29))   # None (ano comum, dia inválido)
print(day_of_year(2023, 13, 1))   # None (mês inválido)
print(day_of_year(2024, 1, 1))    # 1 (primeiro dia do ano)
