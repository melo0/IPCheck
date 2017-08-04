import os, re, time
import multiprocessing
from multiprocessing import process

def ping(IP):
    check = re.search('Reply',os.popen('ping -n 1 {}'.format(IP)).read())
    if  check != None:
        wynik = 'Available'
    else:
        wynik = 'Absent'
    return wynik

def foo_pool(x):
    return ('Ping from '+x+' is {}'.format(ping(x))+'\n')

def log_result(result):
    plik.write(result)
    
def apply_async_with_callback():
    pool=multiprocessing.Pool(processes = 16)
    for i in lista:
        pool.apply_async(foo_pool, args = (i, ), callback = log_result)
    pool.close()
    pool.join()
    return


if __name__ == '__main__':
    plik = open('ping.txt', 'a')
    plik_lista = open('lista.txt', 'r')
    plik.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
    lista = [x for x in (plik_lista.read().split('\n'))]
    apply_async_with_callback()
    plik.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
    plik.write('##############################################################\n\n\n')
    plik.close()
    plik_lista.close()
