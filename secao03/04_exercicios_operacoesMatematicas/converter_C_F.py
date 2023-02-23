
#Converter uma temperatura de graus °C para ºF e para K.
#Dados: ºF = ºC * 1.8 + 32, K = ºC + 273.15

# ºF = ºC * 1.8 + 32 -> conversão
tempC = float(input('Temperatura em °C: '))
tempF = tempC * 1.8 + 32
print(f'A temperatura em °F é: {tempF} °F\n')

#  K = °C + 273.15
tempC = float(input('Temperatura em °C: '))
tempK = tempC + 273.15
print(f'A temperatura em  K é: {tempK}K')
