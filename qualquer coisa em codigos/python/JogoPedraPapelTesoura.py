import pygame
import sys
from random import randint
from time import time

# Inicializar pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pedra, Papel e Tesoura")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (70, 130, 180)
VERDE = (34, 139, 34)
VERMELHO = (220, 20, 60)
CINZA = (128, 128, 128)
AMARELO = (255, 215, 0)

# Fontes
fonte_titulo = pygame.font.Font(None, 48)
fonte_texto = pygame.font.Font(None, 36)
fonte_botao = pygame.font.Font(None, 32)
fonte_grande = pygame.font.Font(None, 72)

# Estados do jogo
MENU = 0
JOGANDO = 1
RESULTADO = 2
ANIMACAO = 3

class JogoPedraPapelTesoura:
    def __init__(self):
        self.estado = MENU
        self.jogador_escolha = None
        self.computador_escolha = None
        self.resultado = ""
        self.animacao_inicio = 0
        self.animacao_texto = ""
        self.placar_jogador = 0
        self.placar_computador = 0
        
        # Opções do jogo
        self.opcoes = ['Pedra', 'Papel', 'Tesoura']
        self.emojis = ['🗿', '📄', '✂️']
        
        # Botões
        self.botoes = {
            'pedra': pygame.Rect(150, 400, 120, 80),
            'papel': pygame.Rect(340, 400, 120, 80),
            'tesoura': pygame.Rect(530, 400, 120, 80),
            'jogar_novamente': pygame.Rect(300, 500, 200, 50)
        }
    
    def desenhar_botao(self, rect, texto, cor_fundo, cor_texto):
        pygame.draw.rect(tela, cor_fundo, rect)
        pygame.draw.rect(tela, PRETO, rect, 3)
        
        texto_surface = fonte_botao.render(texto, True, cor_texto)
        texto_rect = texto_surface.get_rect(center=rect.center)
        tela.blit(texto_surface, texto_rect)
    
    def desenhar_escolha(self, escolha, x, y, titulo):
        # Desenhar título
        titulo_surface = fonte_texto.render(titulo, True, PRETO)
        titulo_rect = titulo_surface.get_rect(centerx=x, y=y-60)
        tela.blit(titulo_surface, titulo_rect)
        
        # Desenhar emoji grande
        if escolha is not None:
            emoji_surface = fonte_grande.render(self.emojis[escolha], True, PRETO)
            emoji_rect = emoji_surface.get_rect(centerx=x, y=y)
            tela.blit(emoji_surface, emoji_rect)
            
            # Desenhar nome da escolha
            nome_surface = fonte_texto.render(self.opcoes[escolha], True, PRETO)
            nome_rect = nome_surface.get_rect(centerx=x, y=y+80)
            tela.blit(nome_surface, nome_rect)
    
    def determinar_vencedor(self):
        if self.jogador_escolha == self.computador_escolha:
            return "EMPATE!"
        elif (self.jogador_escolha == 0 and self.computador_escolha == 2) or \
             (self.jogador_escolha == 1 and self.computador_escolha == 0) or \
             (self.jogador_escolha == 2 and self.computador_escolha == 1):
            self.placar_jogador += 1
            return "VOCÊ VENCEU!"
        else:
            self.placar_computador += 1
            return "COMPUTADOR VENCEU!"
    
    def processar_evento(self, evento):
        if evento.type == pygame.QUIT:
            return False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            if self.estado == MENU:
                # Verificar cliques nos botões de escolha
                if self.botoes['pedra'].collidepoint(mouse_pos):
                    self.jogador_escolha = 0
                    self.iniciar_animacao()
                elif self.botoes['papel'].collidepoint(mouse_pos):
                    self.jogador_escolha = 1
                    self.iniciar_animacao()
                elif self.botoes['tesoura'].collidepoint(mouse_pos):
                    self.jogador_escolha = 2
                    self.iniciar_animacao()
            
            elif self.estado == RESULTADO:
                # Botão jogar novamente
                if self.botoes['jogar_novamente'].collidepoint(mouse_pos):
                    self.estado = MENU
                    self.jogador_escolha = None
                    self.computador_escolha = None
        
        return True
    
    def iniciar_animacao(self):
        self.estado = ANIMACAO
        self.animacao_inicio = time()
        self.computador_escolha = randint(0, 2)
    
    def atualizar(self):
        if self.estado == ANIMACAO:
            tempo_decorrido = time() - self.animacao_inicio
            
            if tempo_decorrido < 1:
                self.animacao_texto = "JO"
            elif tempo_decorrido < 2:
                self.animacao_texto = "KEN"
            elif tempo_decorrido < 3:
                self.animacao_texto = "PÔ!!!"
            else:
                self.resultado = self.determinar_vencedor()
                self.estado = RESULTADO
    
    def desenhar(self):
        tela.fill(BRANCO)
        
        # Título
        titulo = fonte_titulo.render("PEDRA, PAPEL E TESOURA", True, AZUL)
        titulo_rect = titulo.get_rect(centerx=LARGURA//2, y=50)
        tela.blit(titulo, titulo_rect)
        
        # Placar
        placar_texto = f"Você: {self.placar_jogador}  |  Computador: {self.placar_computador}"
        placar_surface = fonte_texto.render(placar_texto, True, PRETO)
        placar_rect = placar_surface.get_rect(centerx=LARGURA//2, y=100)
        tela.blit(placar_surface, placar_rect)
        
        if self.estado == MENU:
            # Instruções
            instrucao = fonte_texto.render("Escolha sua jogada:", True, PRETO)
            instrucao_rect = instrucao.get_rect(centerx=LARGURA//2, y=300)
            tela.blit(instrucao, instrucao_rect)
            
            # Botões de escolha
            self.desenhar_botao(self.botoes['pedra'], "🗿 PEDRA", CINZA, PRETO)
            self.desenhar_botao(self.botoes['papel'], "📄 PAPEL", CINZA, PRETO)
            self.desenhar_botao(self.botoes['tesoura'], "✂️ TESOURA", CINZA, PRETO)
        
        elif self.estado == ANIMACAO:
            # Animação JO-KEN-PÔ
            animacao_surface = fonte_grande.render(self.animacao_texto, True, VERMELHO)
            animacao_rect = animacao_surface.get_rect(center=(LARGURA//2, ALTURA//2))
            tela.blit(animacao_surface, animacao_rect)
        
        elif self.estado == RESULTADO:
            # Mostrar escolhas
            self.desenhar_escolha(self.jogador_escolha, 200, 250, "SUA ESCOLHA")
            self.desenhar_escolha(self.computador_escolha, 600, 250, "COMPUTADOR")
            
            # Mostrar resultado
            cor_resultado = VERDE if "VENCEU" in self.resultado else VERMELHO if "COMPUTADOR" in self.resultado else AMARELO
            resultado_surface = fonte_titulo.render(self.resultado, True, cor_resultado)
            resultado_rect = resultado_surface.get_rect(centerx=LARGURA//2, y=400)
            tela.blit(resultado_surface, resultado_rect)
            
            # Botão jogar novamente
            self.desenhar_botao(self.botoes['jogar_novamente'], "JOGAR NOVAMENTE", AZUL, BRANCO)

def main():
    clock = pygame.time.Clock()
    jogo = JogoPedraPapelTesoura()
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            rodando = jogo.processar_evento(evento)
        
        jogo.atualizar()
        jogo.desenhar()
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
