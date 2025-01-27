from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pygame import mixer
import random
import time

# 3 koła ratunkowe w pasku menu, po ich kliknięciu wyświetla się info że one coś tam robią
def tele():
    messagebox.showinfo("Dzwonimy do Twojego przyjaciela", "H: Witaj! Z tej strony Hubert Urbański z Milionerów.\nTwój przyjaciel gra właśnie o milion i potrzebuje Twojej pomocy przy pytaniu.\nMasz do dyspozycji 4 odpowiedzi.\nP: Myślę, że poprawna jest odpowiedź'...\ni jestem tego pewny na... Mogę się jednak mylić...\n")
def pol_na_pol():
    messagebox.showinfo("50/50", "Proszę o odrzucenie 2 błędnych odpowiedzi.\nDo wyboru pozostały:")
def publicznosc():
    messagebox.showinfo("pomoc publicznosci", "Proszę publiczność o zagłosowanie na poprawną państwa zdaniem odpowiedź.\nOto wyniki procentowe kolejno dla odp A, B, C i D:")

# prowadzący po kliknięciu wyżwietla info o hubercie, takie jego cv i autopromocja ;-)
def akcjaAutor():
    messagebox.showinfo("Hubert", "jestem hubert urbański i prowadzę grę milionerzy w tvn\nod pon. do pt. o 20.55\nZapraszam!")

def akcja_przycisk ():
    print ("Czesc")


glowne_okno=Tk()

# dźwięk
file = 'milionmusic.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()


# tworzone zdjęcie huberta
canvas_width = 330
canvas_height =300
plotno = Canvas(glowne_okno,
           width=canvas_width,
           height=canvas_height)
plotno.pack(side=TOP)
img = Image.open("h.jpg")
img = img.resize((320,320))
imgTk = ImageTk.PhotoImage(img)
plotno.create_image(200,200,image=imgTk)

pasekMenu = Menu(glowne_okno)
peirwszeMenu = Menu(pasekMenu, tearoff=0)

# nazwy okienek u góry(tytuły) po wcisnieciu poszczególnych kół z menu
peirwszeMenu.add_command(label="Telefon do przyjaciela", command=tele)
peirwszeMenu.add_command(label="pół na pół", command=pol_na_pol)
peirwszeMenu.add_command(label="publicznosc", command=publicznosc)

# dalsze menu po lewej u góry co się wyświetla
peirwszeMenu.add_command(label="wyjdz", command=glowne_okno.quit)
pasekMenu.add_cascade(label="koła ratunkowe", menu=peirwszeMenu)
pomocMenu = Menu(pasekMenu, tearoff=0)
pomocMenu.add_command(label="info o prowadzącym", command=akcjaAutor)
pasekMenu.add_cascade(label="Prowadzący", menu=pomocMenu)
glowne_okno.config(menu=pasekMenu)

glowne_okno.title("OKNO GRY")
glowne_okno.geometry("700x550")

# to te przyciski odpowiedzi A B C D i ten tekst nad nimi, 
# ladne kolorki, nie? mogą zostać
v = IntVar()
v.set(0)  # to zazanaczona wartosc początkowa czyli 0 = odpowiedzi A
languages = [
    ("A"),
    ("B"),
    ("C"),
    ("D")
]
def ShowChoice():
    print(v.get())
Label(glowne_okno,
         text="""Poprawna odpowiedź na to pytanie to... :""",
         font=("Times New Roman",11,"italic"),
         padx = 20).pack(side=TOP)
# wygląd przycisków A B C D i ich umiejscowienie
for val, language in enumerate(languages):
    Radiobutton(glowne_okno,
                  text=language,
                  indicatoron = 0,
                  width = 20,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  font=("Curier",10,"bold"),
                  bg = "light blue",
                  activebackground = "dark red",
                  value=val).pack(anchor=S)


glowne_okno.mainloop()
