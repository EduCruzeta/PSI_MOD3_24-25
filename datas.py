import datetime

#data hoje
print(datetime.date.today())

#ano
print(datetime.date.today().year)

#mês
print(datetime.date.today().month)

#dia
print(datetime.date.today().day)

#data e hora
print(datetime.datetime.now())

#como string
print(datetime.datetime.now().strftime("%d - %m - %Y %H:%M:%S "))