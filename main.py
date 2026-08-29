from Streaming import PlataformaStreaming
plataforma = PlataformaStreaming()


while True:
    print("1 --- Cadastrar novo Assinante ---")
    print("2 --- Listar Assinantes ---")
    print("3 --- Cancelar Assinatura ---")
    print("4 --- Sair ---")
  
    opcao = int(input(" Escolha uma opção: "))



    match opcao:
        case 1:
            plataforma.cadastro()
            print("Cadastro concluido com sucesso")


        case 2:
            plataforma.listar_assinantes()


        case 3:
            id_conta = int(input("Informe o ID da conta que deseja cancelar: "))
            resultado = plataforma.cancelar_assinatura(id_conta)

            if resultado:
                print("Assinatura cancelada com sucesso!")

            else:
                print("Assinante não encontrado.")

        case 4:
            break

        case _:
            print("Opção inválida")

                           
            





   
