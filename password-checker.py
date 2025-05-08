# Definindo cores como constantes globais
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

def pass_checker(password):
    # Emojis e símbolos
    LOCK = "🔒"
    CHECK = "✅"
    WARN = "⚠️"
    ERROR = "❌"
    STRONG = "🛡️"
    MEDIUM = "🔑"
    WEAK = "💀"
    RULES = "📜"
    
    # Inicialização de variáveis
    upperChars = lowerChars = specialChars = digits = length = 0
    length = len(password)
    
    # Cabeçalho visual
    print(f"\n{BLUE}╔{'═'*50}╗")
    print(f"║{WHITE}{LOCK:^50}{BLUE}║")
    print(f"║{WHITE} VERIFICADOR DE FORÇA DE SENHA {CYAN}1.0 {WHITE:>15}{BLUE}║")
    print(f"╚{'═'*50}╝{RESET}\n")
    
    # Verificação de comprimento
    if length < 6:
        print(f"{ERROR} {RED}SENHA MUITO CURTA! {RESET}")
        print(f"{WARN} {YELLOW}A senha deve ter no mínimo 6 caracteres{RESET}")
        print(f"{WARN} {YELLOW}Sua senha tem apenas {length} caracteres{RESET}\n")
        return
    
    # Análise dos caracteres
    for char in password:
        if char.isupper(): upperChars += 1
        elif char.islower(): lowerChars += 1
        elif char.isdigit(): digits += 1
        else: specialChars += 1
    
    # Resultado da verificação
    print(f"{RULES} {MAGENTA}REQUISITOS DA SENHA{RESET}")
    print(f"{CHECK if upperChars else ERROR} {CYAN}Letras maiúsculas: {upperChars or 'Faltando'}")
    print(f"{CHECK if lowerChars else ERROR} {CYAN}Letras minúsculas: {lowerChars or 'Faltando'}")
    print(f"{CHECK if digits else ERROR} {CYAN}Números: {digits or 'Faltando'}")
    print(f"{CHECK if specialChars else ERROR} {CYAN}Caracteres especiais: {specialChars or 'Faltando'}")
    print(f"{CHECK if length >=6 else ERROR} {CYAN}Tamanho mínimo (6): {length}")
    print(f"{CHECK if length >=10 else WARN} {CYAN}Tamanho ideal (10+): {length}\n")
    
    # Classificação da força
    if all([upperChars, lowerChars, digits, specialChars]):
        if length >= 12:
            print(f"{STRONG} {GREEN}FORÇA: EXCELENTE! {WHITE}(Score: 10/10){RESET}")
            print(f"{GREEN}Parabéns! Sua senha atende todos os critérios de segurança{RESET}")
        elif length >= 10:
            print(f"{STRONG} {GREEN}FORÇA: FORTE {WHITE}(Score: 8/10){RESET}")
            print(f"{GREEN}Boa senha! Considere aumentar para 12+ caracteres{RESET}")
        else:
            print(f"{MEDIUM} {YELLOW}FORÇA: MÉDIA {WHITE}(Score: 6/10){RESET}")
            print(f"{YELLOW}Senha aceitável, mas poderia ser mais longa{RESET}")
    else:
        print(f"{WEAK} {RED}FORÇA: FRACA {WHITE}(Score: {2 if length >=6 else 0}/10){RESET}")
        print(f"{RED}Recomenda-se criar uma nova senha mais segura{RESET}")
    
    # Rodapé visual
    print(f"\n{BLUE}╔{'═'*50}╗")
    print(f"║{WHITE} DICAS PARA UMA SENHA FORTE: {BLUE:>22}║")
    print(f"║{CYAN} • Use uma frase fácil de lembrar {BLUE:>18}║")
    print(f"║{CYAN} • Combine maiúsculas, minúsculas e números {BLUE:>7}║")
    print(f"║{CYAN} • Adicione caracteres especiais (@, #, $) {BLUE:>8}║")
    print(f"║{CYAN} • Evite sequências óbvias (123, abc) {BLUE:>11}║")
    print(f"╚{'═'*50}╝{RESET}")

# Interface de entrada

# Interface de entrada
print(f"\n{BLUE}╔{'═'*50}╗")
print(f"║{WHITE} DIGITE SUA SENHA PARA VERIFICAÇÃO {BLUE:>18}║")
print(f"╚{'═'*50}╝{RESET}")
password = input(f"{CYAN}→ {RESET}")
pass_checker(password)
