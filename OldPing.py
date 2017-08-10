import os, re, time
# Sprawdzenie czy odpowiedz PING zwaraca 'Reply' i ustawienie wartosci dla agrumentu 'result'
# Verify that the PING returns 'Reply' and sets the value for the 'result' object.

def ping(IP):
    if re.search('Reply',os.popen('ping -n 1 {}'.format(IP)).read()) != None:
        result = 'Available'
    else:
        result = 'Absent'
    return result

if __name__ == '__main__':
    
    # Otawrcie pliku w trybie dodawania    Opening file in append mode
    
    plik = open('ping.txt', 'a')
    
    # Otawrcie pliku z adresami    Opening file with addresses
    
    plik_lista = open('lista.txt', 'r')
    
    # Dopisanie bierzacej daty     Appending the current date 
    
    plik.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
    
    # Wypelnienie listy adresami z pliku "lista.txt"    Filling the list with addresses from file "lista.txt"
    
    lista = [x for x in (plik_lista.read().split('\n'))]
    
    # Lista adresow do sprawdzenia    list of addresses to check
    
    # lista = ['google.com','NotExistingAddress.eu']
    
    # Petla zapisujaca do pliku 'ping.txt'     Loop that writes to a file 'ping.txt'
    
    for i in lista:
        plik.write('Ping from '+i+' is {}'.format(ping(i))+'\n')
    
    plik.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
    plik.write('##############################################################\n\n\n')
    plik.close()
    plik_lista.close()
