# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.


def bigger_number(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.


def draw_square(n):
    for row in range(n):
        print(n * "*")


def bigger_name(list):
    result = ""
    for name in list:
        if len(name) > len(result):
            result = name
    return result


# 80 reais a lata, 1 litro = 3 metros, cada lata 18 litros


def paint_costs(area):
    can_price = 80
    required_liters = area / 3
    required_cans = required_liters // 18
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * can_price
