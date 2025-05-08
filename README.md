# Verificador de Força de Senha 🔒

Este projeto é um verificador de força de senha desenvolvido em Python que analisa e classifica senhas com base em diversos critérios de segurança. O programa oferece uma avaliação visual detalhada com cores, emojis e um sistema de pontuação.

![Screenshot 2025-05-07 at 23-14-44 Screenshot_2025-05-07_23_14_12 png (PNG Image 1280 × 720 pixels) — Scaled (78%)](https://github.com/user-attachments/assets/89224d07-b828-470c-bbd3-351aa27a8a82)

## 📋 Visão Geral

Projeto desenvolvido para avaliar critérios de segurança em senhas, apresentando resultados com:
- Códigos de cores ANSI
- Sistema de pontuação (0-10)
- Classificação visual (fraca/média/forte)
- Dicas de melhoria

## ✨ Recursos

### 🔍 Análise Completa
- Verificação de múltiplos critérios:
  - ☑️ Letras maiúsculas/minúsculas
  - ☑️ Números e caracteres especiais
  - ☑️ Comprimento mínimo (6) e ideal (10+ caracteres)

### 🎨 Interface Visual
```python
print(f"{BLUE}╔{'═'*50}╗")
print(f"║{WHITE}{LOCK:^50}{BLUE}║")
# ... (código de formatação visual)
```

### 📊 Sistema de Classificação
| Ícone | Classificação   | Pontuação | Condições                          |
|-------|-----------------|-----------|------------------------------------|
| 💀    | Fraca           | 0-3       | Não atende requisitos básicos      |
| 🔑    | Média           | 4-7       | Atende parcialmente os requisitos  |
| 🛡️    | Forte/Excelente | 8-10      | Atende todos critérios de segurança|

## 🛠️ Como Usar

1. Execute o script em terminal compatível com ANSI:
```bash
python password_checker.py
```

2. Insira a senha quando solicitado:
```
╔══════════════════════════════════════════════════╗
║ DIGITE SUA SENHA PARA VERIFICAÇÃO                ║
╚══════════════════════════════════════════════════╝
→ sua_senha_aqui
```

3. Interprete os resultados:
   - ✅ Itens atendidos
   - ⚠️ Recomendações
   - ❌ Problemas críticos

## 📝 Exemplo de Saída

```terminal
📜 REQUISITOS DA SENHA
✅ Letras maiúsculas: 2
❌ Números: Faltando
⚠️ Tamanho ideal (10+): 8

🛡️ FORÇA: MÉDIA (Score: 6/10)
Senha aceitável, mas poderia ser mais longa
```

## 💻 Tecnologias

- **Python 3.10+**
- Códigos ANSI para formatação
- Emojis para feedback visual
- String manipulation avançada

## 🌟 Destaques do Código

```python
# Sistema de pontuação condicional
if all([upperChars, lowerChars, digits, specialChars]):
    if length >= 12:
        print(f"{STRONG} {GREEN}FORÇA: EXCELENTE! {WHITE}(Score: 10/10){RESET}")
    # ... (outras condições)
```

## 📈 Melhorias Futuras

- [ ] Adicionar verificação contra listas de senhas comprometidas
- [ ] Implementar análise de padrões comuns (qwerty, 123456)
- [ ] Criar versão web com Flask/Django
- [ ] Adicionar estimativa de tempo para quebra por brute-force

## 📂 Estrutura do Projeto

```
/password_checker/
│── /docs/               # Documentação adicional
│── password_checker.py  # Script principal
```

## 📌 Notas

> Este projeto foi desenvolvido como demonstração de boas práticas de segurança e manipulação de strings em Python. Não armazena ou transmite as senhas analisadas.
