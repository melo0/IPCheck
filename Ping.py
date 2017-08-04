#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re, time
import multiprocessing


# Sprawdzenie czy odpowiedź PING zwaraca 'Reply' i ustawienie wartości dla agrumentu 'wynik'
# Verifying that the PING returns 'Reply' and sets the value for the 'wynik' object.

def ping(IP):
    check = re.search('Reply',os.popen('ping -n 1 {}'.format(IP)).read())
    if  check != None:
        wynik = 'Available'
    else:
        wynik = 'Absent'
    return wynik

# Funkcja z zadaniami dla worker'ow  The function with the task for workers

def for_workers(x):
    return ('Ping from '+x+' is {}'.format(ping(x))+'\n')

# Funkcja zapisująca do pliku   The function appending to the file "ping.txt"

def lista_wynikow(result):
    plik.write(result)

# Funkcja przetwarzania asynchronicznego    The function of asynchronous processing

def przetwarzanie():
    pool=multiprocessing.Pool(processes = 16)
    for i in lista:
        pool.apply_async(for_workers, args = (i, ), callback = lista_wynikow)
    pool.close()
    pool.join()
    return


if __name__ == '__main__':
# Otawrcie pliku "ping.txt" w trybie dodawania    Opening file "ping.txt" in append mode
    plik = open('ping.txt', 'a')
# Otwarcie pliku z adresami do sprawdzenia      Opening file with addresses to check
    plik_lista = open('lista.txt', 'r')
# Dopisanie czasu rozpoczęcia   Apending time of begining
    plik.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
# Przepisanie adresów z pliku do listy      Rewriting addresses from file to list
    lista = [x for x in (plik_lista.read().split('\n'))]
# Wywołanie funkcij przetwarzania asynchronicznego       Call back the function of asynchronous processing
    przetwarzanie()
# Dopisanie czasu zakonczenia    Appending time of ending
    plik.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
    plik.write('##############################################################\n\n\n')
# Zamknięcie plików     Closing the files
    plik.close()
    plik_lista.close()
