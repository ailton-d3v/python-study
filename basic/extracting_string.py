texto = "Python é legal"
print(texto[0:6])
print(texto[-5:])
print(texto[4:len(texto)])


texto = "Aprender Python é divertido"
partes = texto.split()
print(partes)
print(f"{partes[1]} {partes[2]} {partes[3]}!")
print('----------------------------------------')

unido = " " . join(partes)
print(unido)
