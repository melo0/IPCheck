#!/usr/bin/env python
# -*- coding: utf-8 -*-
import customtkinter
from CTkMenuBar import *

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
    p = subprocess.Popen("ping -n 1 " + host)
    if p.wait():
        return time.strftime("%H:%M:%S") + " - " + host + " - DOWN!!!\n"
    else:
        x = str(subprocess.check_output("ping -n 1 " + host))
        return time.strftime("%H:%M:%S") + " - " + host + ' - UP!!! at IP--> ' +\
            x[x.find('[') + 1:x.find(']')] + '\n'


def for_workers(x):
    return ping(x)


def lista_wynikow(result):
    lista.insert(END, result)


def przetwarzanie(ad):
    pool = multiprocessing.Pool(processes=16)
    for i in ad:
        pool.apply_async(for_workers, args=(i,), callback=lista_wynikow)


def sprawdz():
    okno.geometry("820x540")
    lista.grid(row=2, columnspan=2, stick="wes", pady=5)
    if zrodlo.get() != '':
        plik1 = open(zrodlo.get(), "r")
        lista.delete(0.0, END)
        lista.insert(END, time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
        adresy = [x for x in (plik1.read().split('\n'))]
        przetwarzanie(adresy)
        plik1.close()
    else:
        lista.delete(0.0, END)
        lista.insert(END, 'Wskaż źródło pliku')
    return


def zapisz():
    plik2 = tkinter.filedialog.asksaveasfile(mode='a')
    if not plik2:
        return
    try:
        plik2.write(lista.get(0.0, END))
    finally:
        plik2.close()


def wykres():
    tablica = lista.get(0.0, END)
    tak = tablica.count("UP!!!")
    nie = tablica.count("DOWN!!!")
    if (tak > 0 or nie > 0):
        wartosci = [tak, nie]
        plt.pie(wartosci, labels=('UP', 'Down'), colors=('yellowgreen', 'lightcoral'), autopct='%1.1f%%',
                explode=(0.1, 0), shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()
    else:
        okno.geometry("800x450")
        lista.grid(row=2, stick=W + E)
        lista.delete(0.0, END)
        lista.insert(END, 'Przeprowadź najpierw sprawdzanie')
    return

def clicker(x):
    match x:
        case "Wskaż plik":
            przypisz()
        case "Sprawdź":
            sprawdz()
        case "Zapisz":
            zapisz()
        case "Rysuj wykres":
            wykres()
        case "Koniec":
            koniec()


if __name__ == "__main__":
    okno = customtkinter.CTk()
    text_color = "#1df705"
    color = "#064f11"
    font = customtkinter.CTkFont('Arial monospaced for SAP', 16)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    okno.title("Program Ping")
    okno.geometry("820x170")
    okno.eval("tk::PlaceWindow . center")
    ramka = customtkinter.CTkFrame(okno)
    zrodlo = customtkinter.CTkEntry(
        ramka,
        width=780,
        text_color=text_color,
        font=font
    )
    wersja = customtkinter.CTkLabel(ramka, text="IpCheck ver. 0.7.0 ALPHA")
    lista = customtkinter.CTkTextbox(
        ramka,
        width=780,
        height=360,
        text_color=text_color,
        font=font
    )

    btn = customtkinter.CTkSegmentedButton(
        ramka,
        values=["Wskaż plik", "Sprawdź", "Zapisz", "Rysuj wykres", "Koniec"],
        command=clicker,
        font=font,
        text_color=text_color,
        selected_color=color,
        unselected_hover_color=color
    )

    zrodlo.grid(row=0, columnspan=2, stick="we", padx=10, pady=10,)
    wersja.grid(row=4, stick="w", padx=10, pady=10,)
    ramka.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    btn.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    okno.mainloop()
