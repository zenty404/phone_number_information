# ----------
# Importation:
# ---------- 

from distutils import command
from turtle import left
from unittest import result
from xml.dom.minidom import CharacterData
from art import *
from termcolor import colored
import phonenumbers
from tkinter import *
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import webbrowser

# ----------
# Command :
# ----------

def open_my_channel():
    webbrowser.open_new("https://www.twitch.tv/art_hur421")

def boutton_r():
    resultat1.delete(0, END)
    resultat2.delete(0, END)
    resultat3.delete(0, END)

def rechercher_pays():
    ch_nmber = phonenumbers.parse(phone_number.get(), "CH")
    resultat1.delete(0, END)
    resultat1.insert(0, (geocoder.description_for_number(ch_nmber, "en")))


def rechercher_opérateur():
    service_nmber = phonenumbers.parse(phone_number.get(), "RO")
    resultat2.delete(0, END)
    resultat2.insert(0, (carrier.name_for_number(service_nmber, "en")))

def rechercher_timezone():
    gb_number = phonenumbers.parse(phone_number.get(), "GB")
    resultat3.delete(0,END)
    resultat3.insert(0, (timezone.time_zones_for_number(gb_number)))
    



# ----------
# FENETRE :
# ----------
window = Tk()  # Création de a fenêtr 1e
window.geometry("500x400")
window.title("Phone Finder")  # Titre de la calculatrice
window["bg"] = "#B2B4AC"  # Coleur de la fenêtre
window["relief"] = "raised"  # Profondeur de la fenêtre

# ----------
# crée la frame principale
# ----------
frame = Frame(window, bg='#B2B4AC', height=4)

# creer un titre
label_title = Label(frame, text="Phone Finder", font=("Helvetica", 20), bg='#B2B4AC', fg='black')
label_title.pack()

# creer un input 1
phone_number= Entry(frame, font=("Helvetica", 20), bg='#B2B4AC', fg='black')
phone_number.pack()

# creer un bouton1
find = Button(frame, text="Find The Country", font=("Helvetica", 20), fg='black', command=rechercher_pays)
find.pack(fill=X)

# creer un input 2
resultat1 = Entry(frame, font=("Helvetica", 20), bg='#B2B4AC', fg='black')
resultat1.pack()

# creer un bouton2
find_operateur = Button(frame, text="Find The Operator", font=("Helvetica", 20), fg='black', command=rechercher_opérateur)
find_operateur.pack(fill=X)

# creer un input 3
resultat2 = Entry(frame, font=("Helvetica", 20), bg='#B2B4AC', fg='black')
resultat2.pack()

# creer un bouton3
find_TimeZone = Button(frame, text="Find The Time/Zone", font=("Helvetica", 20), fg='black', command=rechercher_timezone)
find_TimeZone.pack(fill=X)

# creer un input 4
resultat3 = Entry(frame, font=("Helvetica", 20), bg='#B2B4AC', fg='black')
resultat3.pack()

# creation d'une barre de menu
menu_bar = Menu(window)
# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# creer un second menu
file_menu2 = Menu(menu_bar,tearoff=0)
file_menu2.add_command(label="Art_hur421", command=open_my_channel)
menu_bar.add_cascade(label="Crédit", menu=file_menu2)
# configurer la fenetre pour ajouter cette menu bar
window.config(menu=menu_bar)

# creer un bouton reset
reset = Button(frame, text='reset', font=("Helvetica", 20), bg='#B2B4AC', fg='black', command=boutton_r)
reset.pack()

# affciher la frame
frame.pack(expand=YES)

#afficher window
window.mainloop()

