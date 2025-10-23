import hashlib
import json
import os
from getpass import getpass

# Arquivo para armazenar usuários
USERS_FILE = 'users.json'

def load_users():
    """Carrega usuários do arquivo JSON"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Salva usuários no arquivo JSON"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    """Cria hash seguro da senha usando SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    """Registra um novo usuário"""
    print("\n=== REGISTRO DE NOVO USUÁRIO ===")
    users = load_users()
    
    username = input("Digite o nome de usuário: ").strip()
    
    if username in users:
        print("❌ Erro: Usuário já existe!")
        return False
    
    if not username:
        print("❌ Erro: Nome de usuário não pode ser vazio!")
        return False
    
    password = getpass("Digite a senha: ")
    password_confirm = getpass("Confirme a senha: ")
    
    if password != password_confirm:
        print("❌ Erro: As senhas não coincidem!")
        return False
    
    if len(password) < 6:
        print("❌ Erro: A senha deve ter pelo menos 6 caracteres!")
        return False
    
    # Armazena o hash da senha
    users[username] = {
        'password_hash': hash_password(password)
    }
    
    save_users(users)
    print(f"✅ Usuário '{username}' registrado com sucesso!")
    return True

def login():
    """Realiza login do usuário"""
    print("\n=== LOGIN ===")
    users = load_users()
    
    username = input("Digite o nome de usuário: ").strip()
    password = getpass("Digite a senha: ")
    
    if username not in users:
        print("❌ Erro: Usuário não encontrado!")
        return False
    
    password_hash = hash_password(password)
    
    if users[username]['password_hash'] == password_hash:
        print(f"✅ Login realizado com sucesso! Bem-vindo, {username}!")
        return True
    else:
        print("❌ Erro: Senha incorreta!")
        return False

def main():
    """Menu principal"""
    while True:
        print("\n" + "="*40)
        print("SISTEMA DE AUTENTICAÇÃO")
        print("="*40)
        print("1. Registrar novo usuário")
        print("2. Fazer login")
        print("3. Sair")
        print("="*40)
        
        choice = input("Escolha uma opção (1-3): ").strip()
        
        if choice == '1':
            register()
        elif choice == '2':
            if login():
                print("\n🎉 Você está logado no sistema!")
                input("Pressione Enter para continuar...")
        elif choice == '3':
            print("\n👋 Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
