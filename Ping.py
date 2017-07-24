import os, re, time
"""
sprawdzenie czy odpowiedz PING zwaraca 'Reply' i ustawienie wartosci dla agrumentu 'result'
Verify that the PING response returns 'Reply' and sets the value for the 'result' object.
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
	Opening file in append mode
	"""
	plik = open('ping.txt', 'a')
	"""
	dopisanie bierzacej daty
	appending the current date 
	"""
	plik.write(time.strftime("%Y-%m-%d %H:%M")+'\n')
	"""
	lista adresow do sprawdzenia
	list of addresses to check
	"""
	lista = ['google.com','NotExistingAddress.eu']
	""""
	petla zapisujaca do pliku 'ping.txt'
	loop that writes to a file 'ping.txt'
	"""
	for i in lista:
		plik.write('Ping from '+i+' is {}'.format(ping(i))+'\n')
	plik.write('##############################################################\n\n\n')
	plik.close()
