import os, re, time
"""
sprawdzenie czy odpowiedź PING zwaraca 'Reply' i ustawienie wartości dla agrumentu 'wynik'
""""
def ping(IP):
	if re.search('Reply',os.popen('ping -n 1 {}'.format('IP')).read()):
		wynik = 'Available'
	else:
		wynik = 'Absent'
	return wynik

if __name__ == '__main__':
	plik = open('ping.txt', 'a')
	plik.write(time.strftime("%Y-%m-%d %H:%M")+'\n')
	"""
  lista adresów do sprawdzenia
  """
  lista = ['google.com']
	""""
  pętla zapisująca do pliku 'ping.txt'
  """
  for i in lista:
		plik.write('Ping from '+i+' is {}'.format(ping(i))+'\n')
	plik.write('##############################################################\n\n\n')
	plik.close()
	
