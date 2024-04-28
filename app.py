import os

restaurantes = ['Pizza','Sushi']
def exibir_nome_do_programa():
    print('Sabor Express\n')
def exibir_opcoes():
    print('1. Cadastrar restaurante.')
    print('2. Listar restaurante.')
    print('3. Ativar restaurante.')
    print('4. Sair.')

def finalizar__app():
    exibir_subtitulo('Finalizar app\n')
def voltar_ao_menu_principal():
    input('\nDigite uma tecla oara voltar para o menu principal: ')
    main()
def opcao_invalida():
    print('Opção inválida.\n')
    voltar_ao_menu_principal()
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja começar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')
        
    voltar_ao_menu_principal()
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            print('Cadastrar novo restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Liste restaurante: ')
            print(restaurantes)
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            finalizar__app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()