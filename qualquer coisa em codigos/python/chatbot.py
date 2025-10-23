import re
import random
from datetime import datetime

class ChatBotL:
    def __init__(self):
        self.name = 'AssistBot'
        self.respondes = {
            'saudacao': [
                'Olá! Como posso ajuda-lo hoje?',
                'Oi! Em que posso ser util?',
                'Olá! Seja bem-vindo! Como posso ajudar?',
                'Oi! Prazer em falar com voce!'
            ],
            'despedida': [
                'Tchau Foi um prazer em conhecer voce!',
                'Até logo! Volte sempre!',
                'Adeus! Tenha um ótimo dia!',
                'Até mais! Estarei aqui quando precisar!'
            ],
            'nome': [
                f'Meu nome é {self.name}! Sou seu assistente virtual',
                f'Eu sou o {self.name}, prazer em conhece-lo!',
                f'Pode me chamar de {self.name}!'
            ],
            'como_esta': [
                'Estou funcionando perfeitamente, obrigado por perguntar!',
                'Estou bem e pronto para ajudar!',
                'Ótimo! E voce, como esta?',
                'Estou excelente! Como posso ajuda-lo?'
            ],
            'tempo': [
                f'Agora sao {datetime.now().strftime('%H:%M') do dia {datetime.now().strftime('%d/%m/%Y')}}',
                f'O horario atual é {datetime.now().strftime('%H:%M')}'
            ],
            'ajuda': [
                'Posso ajudar com consversas basicas! Tente perguntar sobre meu nome, como eu estou, que horas sao, ou apenas converse comigo!'
                'Estou aqui para conversar! Pergunte sobre mim, o tempo, ou qualquer coisa que queira saber!'
                'Posso responder perguntas basicas e manter uma conversa. O que gostaria de saber?'
            ],
            'matematica': [
                'Posso fazer calculos basicos! Digite algo como '2 + 2' ou ' 10 * 5'',
                'Que calculo gostaria que eu fizesse?'
            ],
            'default': [
                'Interessante! Pode me contar mais sobre isso?'
                'Hmm, nao tenho certeza sobre isso. Pode reformular a pergunta?'
                'Desculpe, nao entendi completamente. Pode tentar de outra forma?'
                'Nao tenho essas informações sobre isso no momento. Que tal perguntarmos outra coisa?'
            ]
        }

        self.patterns = {
            'saudacao': r'\b(oi|olá|ola|opa|eae|eai|bom dia|boa tarde|boa noite)\b',
            'despedida': r'\b(tchau|adeus|ate logo|até logo|flw|bye|falou)\b',
            'nome': r'\b(seu nome| como.*chama|qual.*nome|quem.*voce)\b',
            'como_esta': r'\b(como.*esta|como.*vai|tudo bem|como.*voce)\b',
            'tempo':
        }