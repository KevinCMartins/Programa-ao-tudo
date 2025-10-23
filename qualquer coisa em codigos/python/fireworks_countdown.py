import time
import random
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text, width=80):
    print(text.center(width))

def create_firework():
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    firework_chars = ['*', '✦', '✧', '✨', '⭐', '🎆', '🎇']
    
    firework = []
    for _ in range(7):
        line = ""
        for _ in range(random.randint(15, 25)):
            color = random.choice(colors)
            char = random.choice(firework_chars)
            line += color + char + " "
        firework.append(line)
    
    return firework

def countdown_animation():
    print(Fore.CYAN + Style.BRIGHT + "🎆 CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIO! 🎆")
    print()
    time.sleep(2)
    
    for i in range(10, 0, -1):
        clear_screen()
        
        # Cabeçalho
        print(Fore.YELLOW + Style.BRIGHT + "=" * 80)
        print_centered(Fore.CYAN + Style.BRIGHT + "🎆 FOGOS DE ARTIFÍCIO 🎆")
        print(Fore.YELLOW + Style.BRIGHT + "=" * 80)
        print()
        
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        number_color = colors[i % len(colors)]
        
        print()
        print_centered(number_color + Style.BRIGHT + f"╔══════════════════╗")
        print_centered(number_color + Style.BRIGHT + f"║                  ║")
        print_centered(number_color + Style.BRIGHT + f"║        {i:2d}        ║")
        print_centered(number_color + Style.BRIGHT + f"║                  ║")
        print_centered(number_color + Style.BRIGHT + f"╚══════════════════╝")
        print()
        
        sparkles = ['✨', '⭐', '🌟', '💫', '✦', '✧']
        sparkle_line = ""
        for _ in range(20):
            sparkle_line += random.choice(colors) + random.choice(sparkles) + " "
        
        print_centered(sparkle_line)
        print()
        
        if i <= 3:
            print_centered(Fore.RED + Style.BRIGHT + "🔥 PREPARAR... 🔥")
        elif i <= 6:
            print_centered(Fore.YELLOW + Style.BRIGHT + "⚡ QUASE LÁ... ⚡")
        else:
            print_centered(Fore.GREEN + Style.BRIGHT + "🎯 CONTANDO... 🎯")
        
        time.sleep(1)
    
    # EXPLOSÃO FINAL!
    clear_screen()
    
    for explosion in range(5):
        clear_screen()
        
        print(Fore.YELLOW + Style.BRIGHT + "=" * 80)
        print_centered(Fore.RED + Style.BRIGHT + "🎆 FELIZ ANO NOVO! 🎆")
        print(Fore.YELLOW + Style.BRIGHT + "=" * 80)
        print()
        
        fireworks = [create_firework() for _ in range(3)]
        
        max_lines = max(len(fw) for fw in fireworks)
        for line_idx in range(max_lines):
            combined_line = ""
            for fw in fireworks:
                if line_idx < len(fw):
                    combined_line += fw[line_idx][:25]
                else:
                    combined_line += " " * 25
            print_centered(combined_line)
        
        print()
        print_centered(Fore.MAGENTA + Style.BRIGHT + "🎉 BOOM! BOOM! BOOM! 🎉")
        print_centered(Fore.CYAN + Style.BRIGHT + "✨ QUE TODOS OS SEUS SONHOS SE REALIZEM! ✨")
        
        time.sleep(0.8)
    
    clear_screen()
    print(Fore.RAINBOW if hasattr(Fore, 'RAINBOW') else Fore.YELLOW + Style.BRIGHT + "=" * 80)
    print()
    print_centered(Fore.RED + Style.BRIGHT + "🎆 FELIZ ANO NOVO! 🎆")
    print_centered(Fore.YELLOW + Style.BRIGHT + "🎉 QUE 2024 SEJA INCRÍVEL! 🎉")
    print_centered(Fore.GREEN + Style.BRIGHT + "✨ MUITO AMOR E PROSPERIDADE! ✨")
    print_centered(Fore.BLUE + Style.BRIGHT + "🌟 OBRIGADO POR CELEBRAR CONOSCO! 🌟")
    print()
    
    final_firework = create_firework()
    for line in final_firework:
        print_centered(line)
    
    print()
    print(Fore.YELLOW + Style.BRIGHT + "=" * 80)

def main():
    try:
        print(Fore.GREEN + Style.BRIGHT + "Iniciando contagem regressiva dos fogos de artifício...")
        print(Fore.CYAN + "Pressione Ctrl+C para sair a qualquer momento")
        print()
        time.sleep(2)
        
        countdown_animation()
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n🎆 Até a próxima celebração! 🎆")
    except Exception as e:
        print(Fore.RED + f"\nErro durante a execução: {e}")

if __name__ == "__main__":
    main()
