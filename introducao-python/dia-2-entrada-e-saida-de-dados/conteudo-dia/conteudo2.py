numeros = input("Insira seus numeros separando eles por um espaco")

result = numeros.split(" ")

result = 0

for number in numeros:
    if not number.isdigit():
        print(f"Erro ao somar valores, {number} é um valor inválido")
    else:
        result += int(number)

print(f"a soma dos numeros e {result}")
