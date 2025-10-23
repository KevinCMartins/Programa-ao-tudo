import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Inicializar o pygame
pygame.mixer.init()

# Lista de músicas
playlist = []
indice_atual = 0

# Função para carregar várias músicas
def carregar_musicas():
    global playlist, indice_atual
    arquivos = filedialog.askopenfilenames(filetypes=[("Palm City- TimeLesz.mp3", "rah_band_messages_from_the_stars_slowed_+_reverb_mp3_18320.mp3")])
    if arquivos:
        playlist = list(arquivos)
        indice_atual = 0
        tocar_musica()

# Tocar música atual
def tocar_musica():
    if playlist:
        pygame.mixer.music.load(playlist[indice_atual])
        pygame.mixer.music.play()
        nome = os.path.basename(playlist[indice_atual])
        musica_atual.set(f"Tocando: {nome}")
        status.set("Status: Tocando 🎵")

# Próxima música da lista
def proxima_musica():
    global indice_atual
    if playlist:
        indice_atual = (indice_atual + 1) % len(playlist)
        tocar_musica()

# Evento de fim de música
def verificar_fim_musica():
    if not pygame.mixer.music.get_busy() and playlist:
        proxima_musica()
    janela.after(1000, verificar_fim_musica)

# Controles
def pausar():
    pygame.mixer.music.pause()
    status.set("Status: Pausado ⏸️")

def despausar():
    pygame.mixer.music.unpause()
    status.set("Status: Tocando 🎵")

def parar():
    pygame.mixer.music.stop()
    status.set("Status: Parado ⏹️")

# Interface
janela = tk.Tk()
janela.title('Player de Música')
janela.geometry('300x300')
janela.configure(bg='#1e1e1e')

musica_atual = tk.StringVar()
status = tk.StringVar()
musica_atual.set("Nenhuma música")
status.set("Status: Parado")

tk.Label(janela, textvariable=musica_atual, bg='#1e1e1e', fg='white', font=('Arial', 10)).pack(pady=5)
tk.Label(janela, textvariable=status, bg='#1e1e1e', fg='white', font=('Arial', 10, 'bold')).pack(pady=5)

tk.Button(janela, text='🎵 Carregar músicas', width=20, command=carregar_musicas).pack(pady=5)
tk.Button(janela, text='▶️ Tocar', width=20, command=tocar_musica).pack(pady=5)
tk.Button(janela, text='⏸️ Pausar', width=20, command=pausar).pack(pady=5)
tk.Button(janela, text='⏯️ Retomar', width=20, command=despausar).pack(pady=5)
tk.Button(janela, text='⏭️ Próxima', width=20, command=proxima_musica).pack(pady=5)
tk.Button(janela, text='⏹️ Parar', width=20, command=parar).pack(pady=5)

# Iniciar verificação de fim de música
verificar_fim_musica()

janela.mainloop()

