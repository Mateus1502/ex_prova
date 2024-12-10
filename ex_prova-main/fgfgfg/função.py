#Converter temperaturas
def celsius(farenheit):
    C=(farenheit-32) * 5 / 9
    return C
farenheit=int(input('Informe a temperatura em F'))
temperatura_celsius=celsius(farenheit)
print(temperatura_celsius)
def farenheit(celsius):
    F=(celsius * 9 / 5) + 32
    return F
Celsius = int(input('Informe a temperatura em celsius'))
temperatura_farenheit=farenheit(celsius)
print(temperatura_farenheit)
#℃ = (℉ − 32) × 5 ÷ 9 e ℉ = (℃ × 9 ÷ 5
