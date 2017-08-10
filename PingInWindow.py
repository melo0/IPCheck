#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import * 
from tkinter import ttk
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
        return "Time: "+ time.strftime("%H:%M:%S")+" - " + host + " - DOWN!!!\n"
    else:
        return "Time: "+ time.strftime("%H:%M:%S")+" - " + host + "  - UP!!!\n"


def for_workers(x):
    return ping(x)


def lista_wynikow(result):
    lista.insert(END, result)
    
    
def przetwarzanie(ad):
    pool=multiprocessing.Pool(processes = 16)
    for i in ad:
        pool.apply_async(for_workers, args = (i, ), callback = lista_wynikow)
       

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
    okno.geometry("670x440")
    ramka = ttk.Frame(okno, padding = (10,10,10,10))
    zrodlo = tkinter.Entry(ramka)
    lista = tkinter.Text(ramka)
    menubar = Menu(okno)
    filemenu = Menu(menubar, tearoff = 0)
    editmenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "Wczytaj plik", command = przypisz)
    filemenu.add_command(label = "Zamknij", command = koniec)
    editmenu.add_command(label = "Sprawdź", command = sprawdz)
    menubar.add_cascade(label = "Plik", menu = filemenu)
    menubar.add_cascade(label = "Opcje", menu = editmenu)
    okno.config(menu = menubar)
    zrodlo.grid(row = 0, column = 0, stick = W+E)
    lista.grid(row = 1,  stick = W)
    ramka.pack()
    okno.mainloop()
