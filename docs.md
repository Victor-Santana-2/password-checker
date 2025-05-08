# 📝 Documentação Técnica Detalhada do Verificador de Senha

## 🔍 Visão Geral
Script Python que analisa a robustez de senhas utilizando:
- Códigos ANSI para colorização
- Emojis para feedback visual
- Sistema de pontuação de 0 a 10
- Classificação em 3 níveis de segurança

## 🎨 Códigos de Cores ANSI

```python
RED = "\033[1;31m"      # Erros críticos
GREEN = "\033[1;32m"    # Sucesso
YELLOW = "\033[1;33m"   # Alertas
BLUE = "\033[1;34m"     # Cabeçalhos
MAGENTA = "\033[1;35m"  # Títulos
CYAN = "\033[1;36m"     # Informações
WHITE = "\033[1;37m"    # Texto principal
RESET = "\033[0m"       # Resetar formatação
```

## 🔧 Função Principal: `pass_checker(password)`

### 📊 Variáveis de Análise
```python
upperChars = 0    # Contador de maiúsculas
lowerChars = 0    # Contador de minúsculas 
digits = 0        # Contador de números
specialChars = 0  # Contador de caracteres especiais
length = len(password)  # Tamanho total
```

### 🔍 Lógica de Verificação
```python
for char in password:
    if char.isupper(): upperChars += 1
    elif char.islower(): lowerChars += 1
    elif char.isdigit(): digits += 1
    else: specialChars += 1
```

### 📈 Sistema de Pontuação
| Critério            | Peso  | Condição Ideal |
|---------------------|-------|----------------|
| Tamanho ≥ 6         | 1     | Sim            |
| Tamanho ≥ 10        | 2     | Sim            |  
| Maiúsculas          | 1     | ≥ 1            |
| Minúsculas          | 1     | ≥ 1            |
| Números             | 1     | ≥ 1            |
| Caracteres Especiais| 2     | ≥ 1            |

### 🏆 Classificação Final
```python
if score >= 8:
    return "🛡️ FORTE"
elif score >= 5:
    return "🔑 MÉDIA"
else:
    return "💀 FRACA"
```

## 💻 Interface do Usuário

### 📥 Entrada de Dados
```python
print(f"{BLUE}╔{'═'*50}╗")
print(f"║{WHITE} DIGITE SUA SENHA PARA VERIFICAÇÃO {BLUE:>18}║")
password = input(f"{CYAN}→ {RESET}")
```

### 📊 Exemplo de Saída
```terminal
📜 REQUISITOS:
✅ Maiúsculas: 2
✅ Minúsculas: 5
❌ Especiais: 0

🔑 FORÇA: MÉDIA (6/10)
Recomenda-se usar caracteres especiais
```

## 🛠️ Requisitos Técnicos
- Python 3.6+
- Terminal com suporte a ANSI
- Bibliotecas: (nenhuma adicional)

## 🔮 Roadmap
- [ ] Adicionar verificação contra senhas comuns
- [ ] Implementar estimativa de tempo para quebra
- [ ] Criar versão web com Flask

```
> 💡 **Nota:** Todos os exemplos de código estão formatados para Markdown e podem ser usados diretamente em arquivos `.md` ou documentação técnica.
