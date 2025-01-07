import datetime

# Listas para armazenar informações
Clientes = []  
agendamentos = [] 
servicos = {  
    "Corte de cabelo": 50.0,
    "manicure e pedicure": 30.0,
    "Hidratação capilar": 70.0,
    "Maquiagem": 100.0
}
funcionarias = ["Lisa Ketlen", "Andressa Ketlen"]  


def exibir_menu():
    print("\n==== Salão de Beleza ====")
    print("1. Cadastrar Cliente")  
    print("2. Visualizar Clientes")  
    print("3. Agendar serviços")  
    print("4. Consultar agendamentos") 
    print("5. Ver serviços e preços")  
    print("6. Sair")  
    return input("Escolha uma opção: ")

# Função para validar o nome (precisa ter pelo menos duas palavras e não conter números ou caracteres especiais)
def validar_nome(nome):
    if len(nome.split()) < 2:  
        return False
    return nome.replace(" ", "").isalpha()  

# Função para validar o telefone (deve conter 11 dígitos)
def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) == 11

# Função para cadastrar clientes
def cadastrar_clientes():
    nome, telefone = None, None

    # Validação do nome
    while not nome:
        nome_input = input("Digite o nome do cliente (nome e sobrenome): ").strip()
        if not nome_input:  # Verifica se o campo está vazio
            print("O nome é obrigatório. Tente novamente.")
        elif not validar_nome(nome_input):  # Verifica se o nome atende aos critérios
            print("O nome deve conter pelo menos nome e sobrenome, sem números ou caracteres especiais.")
        else:
            nome = nome_input  # Nome válido

    # Validação do telefone
    while not telefone:
        telefone_input = input("Digite o telefone do cliente (com DDD, apenas números): ").strip()
        if not telefone_input:  # Verifica se o campo está vazio
            print("O telefone é obrigatório. Tente novamente.")
        elif not validar_telefone(telefone_input): 
            print("O telefone deve conter exatamente 11 dígitos (2 do DDD + 9 do número). Tente novamente.")
        else:
            telefone = telefone_input  # Telefone válido

  
    Clientes.append({"nome": nome, "telefone": telefone})
    print(f"Cliente {nome} cadastrado com sucesso!")

def visualizar_clientes():
    if not Clientes:  
        print("Nenhum cliente cadastrado")
    else:
        print("\n=== Lista de Clientes ===")
        for i, cliente in enumerate(Clientes, start=1): 
            print(f"{i}. {cliente['nome']} - {cliente['telefone']}")

def agendar_servico():
    if not Clientes: 
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return

    visualizar_clientes()
    while True:
        try:
            cliente_id = int(input("Escolha o cliente pelo número (ou 0 para cancelar): "))
            if cliente_id == 0:  
                return
            cliente = Clientes[cliente_id - 1] 
            break
        except (ValueError, IndexError):  
            print("Cliente inválido. Tente novamente.")

    print("\n=== Serviços Disponíveis ===")
    for i, (servico, preco) in enumerate(servicos.items(), start=1):  
        print(f"{i}. {servico} - R$ {preco:.2f}")
    while True:
        try:
            servico_id = int(input("Escolha o serviço pelo número: "))
            servico_escolhido = list(servicos.keys())[servico_id - 1]
            break
        except (ValueError, IndexError):  
            print("Serviço inválido. Tente novamente.")

    print("\n=== Funcionárias Disponíveis ===")
    for i, funcionaria in enumerate(funcionarias, start=1):  
        print(f"{i}. {funcionaria}")
    while True:
        try:
            fun_id = int(input("Escolha a funcionária pelo número: "))
            funcionaria_escolhida = funcionarias[fun_id - 1] 
            break
        except (ValueError, IndexError):  
            print("Funcionária inválida. Tente novamente.")

    while True:
        data = input("Digite a data (dd/mm/yyyy): ").strip()
        try:
            dia, mes, ano = map(int, data.split("/"))
            data_obj = datetime.date(ano, mes, dia)
            if data_obj.weekday() == 0:  
                print("O salão está fechado às segundas-feiras. Escolha outra data.")
                continue
            break
        except (ValueError, IndexError):  
            print("Data inválida. Tente novamente no formato dd/mm/yyyy.")

    horario = input("Digite o horário (hh:mm): ").strip()
    data_horario = f"{data} {horario}"

   
    agendamentos.append({
        "Cliente": cliente["nome"],
        "servico": servico_escolhido,
        "Funcionaria": funcionaria_escolhida,
        "data_horario": data_horario
    })
    print(f"Serviço agendado para {cliente['nome']} com {funcionaria_escolhida} em {data_horario}")


def consultar_agendamentos():
    if not agendamentos:  
        print("Nenhum agendamento encontrado")
    else:
        print("\n=== Agendamentos ===")
        for i, agendamento in enumerate(agendamentos, start=1): 
            print(f"{i}. {agendamento['data_horario']} - {agendamento['Cliente']} - {agendamento['servico']} com {agendamento['Funcionaria']}")


def ver_servicos():
    print("\n=== Serviços e Preços ===")
    for servico, preco in servicos.items(): 
        print(f"{servico}: R$ {preco:.2f}")


while True:
    opcao = exibir_menu()
    if opcao == "1":
        cadastrar_clientes()
    elif opcao == "2":
        visualizar_clientes()
    elif opcao == "3":
        agendar_servico()
    elif opcao == "4":
        consultar_agendamentos()
    elif opcao == "5":
        ver_servicos()
    elif opcao == "6":
        print("Encerrando o sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
