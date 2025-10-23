import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pygame
import os
import random
from pathlib import Path

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        
        self.playlist = []
        self.indice_atual = 0
        self.volume = 0.7
        self.shuffle_mode = False
        self.repeat_mode = False
        self.posicao_atual = 0
        
        self.setup_interface()
        
    def setup_interface(self):
        self.janela = tk.Tk()
        self.janela.title('🎵 Music Player Pro')
        self.janela.geometry('400x500')
        self.janela.configure(bg='#2b2b2b')
        self.janela.resizable(False, False)
        
        # Variáveis da interface
        self.musica_atual = tk.StringVar(value="Nenhuma música selecionada")
        self.status = tk.StringVar(value="Status: Parado ⏹️")
        self.tempo_atual = tk.StringVar(value="00:00")
        
        self.criar_widgets()
        
    def criar_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.janela, bg='#2b2b2b')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        info_frame = tk.Frame(main_frame, bg='#3b3b3b', relief='raised', bd=2)
        info_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(info_frame, textvariable=self.musica_atual, bg='#3b3b3b', fg='#ffffff', 
                font=('Arial', 11, 'bold'), wraplength=350).pack(pady=10)
        
        tk.Label(info_frame, textvariable=self.status, bg='#3b3b3b', fg='#00ff00', 
                font=('Arial', 10)).pack(pady=(0, 5))
        
        tk.Label(info_frame, textvariable=self.tempo_atual, bg='#3b3b3b', fg='#ffffff', 
                font=('Arial', 9)).pack(pady=(0, 10))
        
        controls_frame = tk.Frame(main_frame, bg='#2b2b2b')
        controls_frame.pack(fill='x', pady=(0, 15))
        
        # Primeira linha de controles
        row1 = tk.Frame(controls_frame, bg='#2b2b2b')
        row1.pack(fill='x', pady=5)
        
        self.criar_botao(row1, '📁 Carregar Músicas', self.carregar_musicas, '#4CAF50')
        
        # Segunda linha de controles
        row2 = tk.Frame(controls_frame, bg='#2b2b2b')
        row2.pack(fill='x', pady=5)
        
        self.criar_botao(row2, '⏮️ Anterior', self.musica_anterior, '#2196F3', side='left')
        self.criar_botao(row2, '▶️ Tocar', self.tocar_musica, '#FF9800', side='left')
        self.criar_botao(row2, '⏸️ Pausar', self.pausar, '#FF5722', side='left')
        
        # Terceira linha de controles
        row3 = tk.Frame(controls_frame, bg='#2b2b2b')
        row3.pack(fill='x', pady=5)
        
        self.criar_botao(row3, '⏭️ Próxima', self.proxima_musica, '#9C27B0', side='left')
        self.criar_botao(row3, '⏹️ Parar', self.parar, '#F44336', side='left')
        self.criar_botao(row3, '🔄 Repetir', self.toggle_repeat, '#607D8B', side='left')
        
        volume_frame = tk.Frame(main_frame, bg='#2b2b2b')
        volume_frame.pack(fill='x', pady=(0, 15))
        
        tk.Label(volume_frame, text='🔊 Volume:', bg='#2b2b2b', fg='white', 
                font=('Arial', 10)).pack(side='left')
        
        self.volume_scale = tk.Scale(volume_frame, from_=0, to=100, orient='horizontal',
                                   bg='#2b2b2b', fg='white', highlightthickness=0,
                                   command=self.ajustar_volume)
        self.volume_scale.set(70)
        self.volume_scale.pack(side='right', fill='x', expand=True, padx=(10, 0))
        
        options_frame = tk.Frame(main_frame, bg='#2b2b2b')
        options_frame.pack(fill='x')
        
        self.shuffle_var = tk.BooleanVar()
        shuffle_check = tk.Checkbutton(options_frame, text='🔀 Modo Aleatório', 
                                     variable=self.shuffle_var, bg='#2b2b2b', fg='white',
                                     selectcolor='#2b2b2b', command=self.toggle_shuffle)
        shuffle_check.pack(side='left')
        
    def criar_botao(self, parent, text, command, color, side='top'):
        btn = tk.Button(parent, text=text, command=command, bg=color, fg='white',
                       font=('Arial', 9, 'bold'), relief='raised', bd=2,
                       activebackground=color, activeforeground='white')
        if side == 'left':
            btn.pack(side='left', padx=2, fill='x', expand=True)
        else:
            btn.pack(fill='x', pady=2)
        return btn
        
    def carregar_musicas(self):
        try:
            arquivos = filedialog.askopenfilenames(
                title="Selecionar músicas",
                filetypes=[
                    ("Arquivos de Áudio", "*.mp3 *.wav *.ogg *.m4a"),
                    ("MP3", "*.mp3"),
                    ("WAV", "*.wav"),
                    ("OGG", "*.ogg"),
                    ("Todos os arquivos", "*.*")
                ]
            )
            
            if arquivos:
                self.playlist = list(arquivos)
                self.indice_atual = 0
                self.atualizar_display()
                messagebox.showinfo("Sucesso", f"{len(arquivos)} música(s) carregada(s)!")
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar músicas: {str(e)}")
    
    def tocar_musica(self):
        if not self.playlist:
            messagebox.showwarning("Aviso", "Nenhuma música carregada!")
            return
            
        try:
            pygame.mixer.music.load(self.playlist[self.indice_atual])
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(self.volume)
            self.atualizar_display()
            self.status.set("Status: Tocando 🎵")
            
        except pygame.error as e:
            messagebox.showerror("Erro", f"Erro ao tocar música: {str(e)}")
    
    def proxima_musica(self):
        if not self.playlist:
            return
            
        if self.shuffle_mode:
            self.indice_atual = random.randint(0, len(self.playlist) - 1)
        else:
            self.indice_atual = (self.indice_atual + 1) % len(self.playlist)
        
        self.tocar_musica()
    
    def musica_anterior(self):
        if not self.playlist:
            return
            
        if self.shuffle_mode:
            self.indice_atual = random.randint(0, len(self.playlist) - 1)
        else:
            self.indice_atual = (self.indice_atual - 1) % len(self.playlist)
        
        self.tocar_musica()
    
    def pausar(self):
        try:
            pygame.mixer.music.pause()
            self.status.set("Status: Pausado ⏸️")
        except:
            pass
    
    def despausar(self):
        try:
            pygame.mixer.music.unpause()
            self.status.set("Status: Tocando 🎵")
        except:
            pass
    
    def parar(self):
        try:
            pygame.mixer.music.stop()
            self.status.set("Status: Parado ⏹️")
        except:
            pass
    
    def ajustar_volume(self, valor):
        self.volume = int(valor) / 100
        pygame.mixer.music.set_volume(self.volume)
    
    def toggle_shuffle(self):
        self.shuffle_mode = self.shuffle_var.get()
    
    def toggle_repeat(self):
        self.repeat_mode = not self.repeat_mode
        if self.repeat_mode:
            messagebox.showinfo("Modo Repetir", "Modo repetir ativado!")
        else:
            messagebox.showinfo("Modo Repetir", "Modo repetir desativado!")
    
    def atualizar_display(self):
        if self.playlist and self.indice_atual < len(self.playlist):
            nome = Path(self.playlist[self.indice_atual]).stem
            self.musica_atual.set(f"♪ {nome}")
        else:
            self.musica_atual.set("Nenhuma música selecionada")
    
    def verificar_fim_musica(self):
        try:
            if not pygame.mixer.music.get_busy() and self.playlist:
                if self.repeat_mode:
                    self.tocar_musica()  # Repetir a mesma música
                else:
                    self.proxima_musica()  # Próxima música
        except:
            pass
        
        self.janela.after(1000, self.verificar_fim_musica)
    
    def executar(self):
        self.verificar_fim_musica()
        self.janela.mainloop()

# Executar o player
if __name__ == "__main__":
    player = MusicPlayer()
    player.executar()
