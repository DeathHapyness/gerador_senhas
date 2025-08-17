import secrets
import string
from colorama import Fore
import sqlite3

def senha_fraca(tamanho=5, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_letters
    if usar_numeros:  
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation 
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

def senha_media(tamanho=10, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_letters
    if usar_numeros:  
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation 
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

def senha_forte(tamanho=20, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

def senha_eh_comum(senha):
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM senhas_comuns WHERE senha = ?", (senha,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def forca_senha(senha):
    pontuacao = 0
    dicas = []

    if len(senha) < 8:
        pontuacao += 1
        dicas.append("Aumente o comprimento da senha")
    elif len(senha) >= 12:
        pontuacao += 3
    else:
        pontuacao += 2
    
    if any(c.isupper() for c in senha):
        pontuacao += 1
    else:
        dicas.append("Adicione pelo menos uma letra maiúscula")

    if any(c.isdigit() for c in senha):
        pontuacao += 1
    else:
        dicas.append("Adicione pelo menos um número")

    if any(c in string.punctuation for c in senha):
        pontuacao += 1
    else:
        dicas.append("Adicione pelo menos um símbolo")

    # Aqui, se você estiver usando senhas comuns:
    if senha_eh_comum(senha):
        pontuacao = min(pontuacao, 2)
        dicas.append("Esta senha é muito comum, tente mudar letras ou adicionar números e símbolos")

    if pontuacao <= 2:
        return "Fraca", Fore.RED + "🔴", dicas
    elif pontuacao <= 4:
        return "Média", Fore.YELLOW + "🟡", dicas
    else:
        return "Forte", Fore.GREEN + "🟢", dicas

    
    
