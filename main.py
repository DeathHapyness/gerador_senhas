from colorama import Fore, Style, init
from funcoes import senha_fraca, senha_media, senha_forte, forca_senha

init(autoreset=True)
print(Fore.CYAN + "Bem vindo ao gerador de senhas:\n===============================================")

modo = input("Deseja gerar senhas ou avaliar sua própria senha? (gerar/avaliar): ").strip().lower()

if modo == "avaliar":
    senha = input("Digite a senha que deseja avaliar: ")
    forca, emoji, dicas = forca_senha(senha)
    print("\nResultado da senha:")
    print(Fore.GREEN + f"SENHA: {senha}")
    print(Fore.GREEN + f"FORÇA: {emoji} {forca}")
    if dicas:
        print(Fore.YELLOW + "Dicas:")
        for dica in dicas:
            print(Fore.YELLOW + f"- {dica}")

elif modo == "gerar":
    # Inputs do usuário
    nivel = input("NÍVEIS DE SENHA:\nFraca = 1\nMédia = 2\nForte = 3\nEscolha um nível: ")
    quantity = input("Quantas senhas deseja gerar? (1-10): ")

    try:
        quantity_num = int(quantity)
        if quantity_num < 1 or quantity_num > 10:
            raise ValueError
    except ValueError:
        print("Quantidade inválida. Usando 1 senha.")
        quantity_num = 1

    if nivel == '1':
        gerar_senha = senha_fraca
    elif nivel == '2':
        gerar_senha = senha_media
    elif nivel == '3':
        gerar_senha = senha_forte
    else:
        print("Nível inválido. Usando senha média por padrão.")
        gerar_senha = senha_media

    senhas_geradas = []
    for _ in range(quantity_num):
        senha = gerar_senha()
        forca, emoji, dicas = forca_senha(senha)
        senhas_geradas.append((senha, forca, emoji, dicas))

    print("\n" + "="*80)
    print(Fore.GREEN + f"{'#':<3} {'SENHA':<25} {'FORÇA':<10} {'DICAS'}")
    print("="*80)
    for i, (senha, forca, emoji, dicas) in enumerate(senhas_geradas, start=1):
        print(Fore.GREEN + f"{i:<3} {senha:<25} {emoji} {forca:<10} {'; '.join(dicas)}")
    print("="*80)

else:
    print("Opção inválida. Encerrando programa.")

print(Fore.CYAN + "Obrigado por usar o gerador de senhas!")

















