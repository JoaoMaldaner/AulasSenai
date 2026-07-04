def fahrenheit_para_celsius(f):
    """Converte temperatura de Fahrenheit para Celsius"""
    celsius = (f - 32) * 5 / 9
    return celsius


fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))


celsius = fahrenheit_para_celsius(fahrenheit)

print(f"{fahrenheit}°F equivalem a {celsius:.2f}°C")