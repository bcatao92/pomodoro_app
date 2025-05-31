import tkinter as tk
from tkinter.ttk import *
from playsound import playsound

janela = tk.Tk()                                #define a janela
janela.title("Pomodoro")
janela.geometry('218x200')                      #define tamanho da janela
icone = tk.PhotoImage(file='tomate.png')        #define imagem do icone
janela.iconphoto(False,icone)                   #define o icone

tempo = tk.IntVar()
contador_var = tk.StringVar(value="")           # variável para exibir a contagem

def tocar_som():
    playsound('sininho.mp3')

def atualizar_contagem(segundos):
    if segundos >= 0:
        minutos = segundos // 60
        seg = segundos % 60
        contador_var.set(f"{minutos:02d}:{seg:02d}")
        if segundos > 0:
            janela.after(1000, atualizar_contagem, segundos - 1)
        else:
            tocar_som()

def pomodoro(tempo):
    espera = tempo.get()
    if espera > 0:
        atualizar_contagem(espera * 60)
    else:
        tocar_som()

img = icone.subsample(45,45)
time_label = tk.Label(janela, text="Digite o tempo que deseja focar: ",font=("calibre",10,"bold"))
entry_label = tk.Entry(janela,textvariable=tempo,font=("calibre",10,"bold"))
contador_label = tk.Label(janela, textvariable=contador_var, font=("calibre", 16, "bold"))
sub_btn = tk.Button(janela, image=img, command=lambda:pomodoro(tempo))

time_label.grid(row=0, column=0, columnspan=2, pady=10)
entry_label.grid(row=1, column=0, columnspan=2, pady=10)
contador_label.grid(row=2, column=0, columnspan=2, pady=10)
sub_btn.grid(row=3, column=0, columnspan=2, pady=20, sticky="nsew")

janela.mainloop()