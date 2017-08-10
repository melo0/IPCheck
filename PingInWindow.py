#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import * 
from tkinter import filedialog
import tkinter.ttk
import os, re, time
import multiprocessing
import subprocess
from tkinter.tix import Shell
from email._header_value_parser import Terminal



def koniec():
    okno.quit()
    okno.destroy()

def przypisz():
    zrodlo.insert(END, tkinter.filedialog.askopenfilename())
    return
    
def ping(host):
    proce = subprocess.Popen("ping -n 1 " + host)
    if proce.wait():
        return host + " - down \n"
    else:
        return host + "  - up \n"

def for_workers(x):
    return ping(x)

def lista_wynikow(result):
    lista.insert(END, result)
    

def przetwarzanie(ad):
    pool=multiprocessing.Pool(processes = 16)
    for i in ad:
        pool.apply_async(for_workers, args = (i, ), callback = lista_wynikow)
        #lista.insert(END, str(ping(i)))


def sprawdz():
    plik1 = open(zrodlo.get(), "r")
    lista.insert(END, time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
    adresy = [x for x in (plik1.read().split('\n'))]
    przetwarzanie(adresy)
    plik1.close()
    return
    

if __name__ == "__main__":
    okno = tkinter.Tk()
    okno.title("Program Ping")
    okno.geometry("700x500")
    zrodlo = tkinter.Entry(okno)
    butt1 = tkinter.Button(okno, text = "  ...  ", command = lambda:przypisz())
    lista = tkinter.Text(okno)
    butt2 = tkinter.Button(okno, text = "Sprawdź", command = lambda: sprawdz())
    butt3 = tkinter.Button(okno, text = "Koniec", command = lambda: koniec())
    zrodlo.grid(row = 0,  stick = W+E)
    butt1.grid(row = 0, column = 2)
    lista.grid(row = 1,  stick = W)
    butt2.grid(row = 2, stick = W)
    butt3.grid(row = 2, stick = E)
    okno.mainloop()
