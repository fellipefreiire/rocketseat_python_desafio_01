contato_invalido = "Índice de contato inválido."

def adicionar_contato(contatos, nome, telefone, email, favorito):
  contato = {
    'nome': nome,
    'telefone': telefone,
    'email': email,
    'favorito': favorito
  }
  contatos.append(contato)
  print(f"Contato {nome} adicionado com sucesso!")

def visualizar_contato(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    favorito = '(favorito)' if contato['favorito'] else ''
    print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']} {favorito}")

def editar_contato(contatos, indice_contato, nome, telefone, email, favorito):
  novo_indice = indice_contato - 1
  if novo_indice >= 0 and novo_indice < len(contatos):
    contatos[novo_indice]['nome'] = nome
    contatos[novo_indice]['telefone'] = telefone
    contatos[novo_indice]['email'] = email
    contatos[novo_indice]['favorito'] = favorito
    print(f"Contato {indice_contato} atualizado para {nome}")
  else:
    print(contato_invalido)

def marcar_contato_como_favorito(contatos, indice_contato):
  novo_indice = indice_contato - 1
  if novo_indice >= 0 and novo_indice < len(contatos):
    contatos[novo_indice]['favorito'] = True
    print(f"Contato {indice_contato} marcado como favorito")
  else:
    print(contato_invalido)

def visualizar_contatos_favoritos(contatos):
  print("\nLista de contatos favoritos:")
  for indice, contato in enumerate(contatos, start=1):
    if contato['favorito']:
      print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}")

def apagar_contato(contatos, indice_contato):
  novo_indice = indice_contato - 1
  if novo_indice >= 0 and novo_indice < len(contatos):
    contatos.pop(novo_indice)
    print(f"Contato {indice_contato} apagado com sucesso")
  else:
    print(contato_invalido)

contatos = []

while True:
  print("\nMenu do gerenciador de contatos:")
  print("1. Adicionar contato")
  print("2. Visualizar contatos")
  print("3. Editar contato")
  print("4. Marcar contato como favorito")
  print("5. Visualizar contatos favoritos")
  print("6. Apagar contato")
  print("7. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    favorito = input("O contato é favorito? (s/n): ")
    favorito = True if favorito == "s" else False
    adicionar_contato(contatos, nome, telefone, email, favorito)
  if escolha == "2":
    visualizar_contato(contatos)
  if escolha == "3":
    visualizar_contato(contatos)
    indice_contato = int(input("Digite o número do contato que deseja editar: "))
    nome = input("Digite o novo nome do contato: ")
    telefone = input("Digite o novo telefone do contato: ")
    email = input("Digite o novo email do contato: ")
    favorito = input("O contato é favorito? (s/n): ")
    favorito = True if favorito == "s" else False
    editar_contato(contatos, indice_contato, nome, telefone, email, favorito)
  if escolha == "4":
    visualizar_contato(contatos)
    indice_contato = int(input("Digite o número do contato que deseja marcar como favorito: "))
    marcar_contato_como_favorito(contatos, indice_contato)
  if escolha == "5":
    visualizar_contatos_favoritos(contatos)
  if escolha == "6":
    visualizar_contato(contatos)
    indice_contato = int(input("Digite o número do contato que deseja apagar: "))
    apagar_contato(contatos, indice_contato)
  if escolha == "7":
    break
