# Cenário:
# O consumo de combustível pode ser expresso de diferentes maneiras:
# - Na Europa: litros por 100 quilômetros (l/100km)
# - Nos EUA: milhas por galão (mpg)
#
# Tarefa:
# Criar duas funções:
# 1. liters_100km_to_miles_gallon → converte l/100km para mpg
# 2. miles_gallon_to_liters_100km → converte mpg para l/100km
#
# Dados de conversão:
# 1 milha = 1609.344 metros
# 1 galão = 3.785411784 litros
#
# Fórmulas:
# mpg = (100 * milhas_por_km) / (litros_por_galao * litros_100km)
# l/100km = (100 * litros_por_galao) / (milhas_por_km * mpg)

def liters_100km_to_miles_gallon(liters):
    # Define as constantes de conversão
    miles_per_km = 1 / 1.609344
    liters_per_gallon = 3.785411784

    # Converte l/100km para mpg
    return (100 * miles_per_km) / (liters * liters_per_gallon)


def miles_gallon_to_liters_100km(miles):
    # Define as constantes de conversão
    km_per_mile = 1.609344
    liters_per_gallon = 3.785411784

    # Converte mpg para l/100km
    return (100 * liters_per_gallon) / (miles * km_per_mile)


# Testes das funções
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
