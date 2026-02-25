# Passo 1: Receber os dados do usuário
usuario = input("Digite o seu nome: ")
cargo = input("Digite o seu cargo (Admin / Estagiario / Outro): ")

# Passo 2: A lógica de decisão (Onde você entra!)
# Dica: Use if, elif e else.

if cargo == "Admin":
    print(f"Olá {usuario}, seu acesso é TOTAL.")

elif cargo == "Estagiario":
    print(f"Olá {usuario}, seu acesso é LIMITADO aos servidores de teste.")

else:
    print("Acesso NEGADO. Procure o administrador do sistema.")