from datetime import datetime, timedelta

# data e hora atual
agora = datetime.now()
print(agora)


# criar uma data especifica
data = datetime(2024, 9, 4, 17, 40, 30, 121554)
print(data)

# adiciona ou subtrai dias, horas...
futuro = agora + timedelta(days=2)
print(futuro)
