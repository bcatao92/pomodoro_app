import time
import tkinter as tk
from tkinter.ttk import *
from playsound import playsound

janela = tk.Tk()                                #define a janela
janela.title("Pomodoro")
janela.geometry('218x200')                      #define tamanho da janela
icone = tk.PhotoImage(file='tomate.png')        #define imagem do icone
janela.iconphoto(False,icone)                   #define o icone

tempo = tk.IntVar()

def tocar_som():
    playsound('sininho.mp3')

def pomodoro(tempo):
    espera = tempo.get()                             #variavel para o tempo
    if espera > 0:
        janela.after(espera*60*1000,tocar_som)
    else:
        tocar_som()




img = icone.subsample(45,45)
time_label = tk.Label(janela, text="Digite o tempo que deseja focar: ",font=("calibre",10,"bold"))
entry_label = tk.Entry(janela,textvariable=tempo,font=("calibre",10,"bold"))
sub_btn = tk.Button(janela, image=img, command=lambda:pomodoro(tempo))

time_label.grid(row=0, column=0, columnspan=2, pady=10)
entry_label.grid(row=1, column=0, columnspan=2, pady=10)
sub_btn.grid(row=2, column=0, columnspan=2, pady=20, sticky="nsew")

janela.mainloop()