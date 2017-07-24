import os, re, time
"""
sprawdzenie czy odpowiedz PING zwaraca 'Reply' i ustawienie wartosci dla agrumentu 'result'
"""
def ping(IP):
	if re.search('Reply',os.popen('ping -n 1 {}'.format(IP)).read()) != None:
		result = 'Available'
	else:
		result = 'Absent'
	return result

if __name__ == '__main__':
	"""
	otawrcie pliku w trybie dodawania
	"""
	plik = open('ping.txt', 'a')
	"""
	dopisanie bierzacej daty
	"""
	plik.write(time.strftime("%Y-%m-%d %H:%M")+'\n')
	"""
	lista adresow do sprawdzenia
	"""
	lista = ['google.com','NieIstniejacyAdres.eu']
	""""
	petla zapisujaca do pliku 'ping.txt'
	"""
	for i in lista:
		plik.write('Ping from '+i+' is {}'.format(ping(i))+'\n')
	plik.write('##############################################################\n\n\n')
	plik.close()
