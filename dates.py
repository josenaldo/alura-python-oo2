################################################################################
# Convertendo de date para string
from datetime import date

# Criando um objeto date com a data atual
data_atual = date.today()
print(data_atual)

# Formatando datas em strings usando o método strftime()
data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)

################################################################################
# Convertendo de datetime para string
from datetime import datetime

data_e_hora_atuais = datetime.now()
print(data_e_hora_atuais)

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
print(data_e_hora_em_texto)

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
print(data_e_hora_em_texto)

################################################################################
# Convertendo de string para datetime
from datetime import datetime

data_e_hora_em_texto = '01/03/2018 12:30'
data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')
print(data_e_hora)

################################################################################
# Lidando com fuso horário
from datetime import datetime, timezone, timedelta

# Criando um objeto datetime com tempo e agora
data_e_hora_atuais = datetime.now()
data_e_hora_atuais_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
print(data_e_hora_atuais_em_texto)

# Criando um timedelta de -3 horas (indicano o fuso horário de São Paulo)
diferenca = timedelta(hours=-5)
print(diferenca)

# Criando o objeto do fuso horário
fuso_horario = timezone(diferenca)
print(fuso_horario)

# Concertendo  o tempo da máquina para o de São Paulo, usando o método astimezone():
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)