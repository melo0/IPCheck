#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
import tkinter.ttk
import time
import multiprocessing
import subprocess
import matplotlib.pyplot as plt


def koniec():
    okno.quit()
    okno.destroy()

def przypisz():
    zrodlo.delete(0, END)
    zrodlo.insert(END, tkinter.filedialog.askopenfilename())
    return
   
def ping(host):
    proce = subprocess.Popen("ping -n 1 " + host)
    if proce.wait():
        return "Time: " + time.strftime("%H:%M:%S") + " - " + host + " - DOWN!!!\n"
    else:
        return "Time: " + time.strftime("%H:%M:%S") + " - " + host + "  - UP!!!\n"

def for_workers(x):
    return ping(x)

def lista_wynikow(result):
    lista.insert(END, result)
      
def przetwarzanie(ad):
    pool=multiprocessing.Pool(processes = 16)
    for i in ad:
        pool.apply_async(for_workers, args = (i, ), callback = lista_wynikow)
       
def sprawdz():
    okno.geometry("670x440")
    lista.grid(row = 1,  stick = W)
    if zrodlo.get() != '':
        plik1 = open(zrodlo.get(), "r")
        lista.delete(0.0, END)
        lista.insert(END, time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
        adresy = [x for x in (plik1.read().split('\n'))]
        przetwarzanie(adresy)
        plik1.close()
    else:
        lista.delete(0.0, END)
        lista.insert(END, 'Wskaż źródło pliku')
    return

def zapisz():
    plik2 = tkinter.filedialog.asksaveasfile(mode = 'a')
    if not plik2:
        return
    try:
        plik2.write(lista.get(0.0, END))
    finally:
        plik2.close()   
    
def wykres():
    tablica = lista.get(0.0, END)
    tak =  tablica.count("UP!!!")
    nie = tablica.count("DOWN!!!")
    if (tak > 0 or nie > 0):
        wartosci = [tak,nie]
        plt.pie(wartosci, labels = ('UP','Down'), colors = ('yellowgreen','lightcoral'), autopct='%1.1f%%', explode = (0.1, 0), shadow = True, startangle = 140)
        plt.axis('equal')
        plt.show()
    else:
        okno.geometry("670x440")
        lista.grid(row = 1, stick = W)
        lista.delete(0.0, END)
        lista.insert(END, 'Przeprowadź najpierw sprawdzanie')
    return


if __name__ == "__main__":
    okno = tkinter.Tk()
    okno.title("Program Ping")
    okno.geometry("650x80")
    ramka = ttk.Frame(okno, padding = (10,10,10,10))
    zrodlo = tkinter.Entry(ramka, width = 104)
    wersja = tkinter.Label(ramka, text = "IpCheck ver. 0.6.5 ALPHA")
    lista = tkinter.Text(ramka)
    menubar = Menu(okno)
    filemenu = Menu(menubar, tearoff = 0)
    editmenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "Wczytaj plik", command = przypisz)
    filemenu.add_command(label = "Zapisz wynik", command = zapisz)
    filemenu.add_command(label = "Zamknij", command = koniec)
    editmenu.add_command(label = "Sprawdź", command = sprawdz)
    editmenu.add_command(label = "Rysuj wykres", command = wykres)
    menubar.add_cascade(label = "Plik", menu = filemenu)
    menubar.add_cascade(label = "Opcje", menu = editmenu)
    okno.config(menu = menubar)
    zrodlo.grid(row = 0, column = 0, stick = W+E)
    wersja.grid(row = 2, stick = W+E)
    ramka.pack(fill = BOTH)
    okno.mainloop()
